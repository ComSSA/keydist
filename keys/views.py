from django.shortcuts import render, redirect, get_object_or_404
from keys.models import *
from keydist.views import *
from django.contrib import messages
from django.utils import timezone
from django.core.mail import send_mail
from django.core.urlresolvers import reverse_lazy
from textwrap import dedent
import xml.etree.ElementTree as ET
import forms

def upload(request):
    if request.method == 'POST':
        form = forms.KeyImportForm(request.POST, request.FILES)
        if form.is_valid():
            root = ET.fromstring(request.FILES['keyfile'].read())[0]
            # Find the SKU listed in the file.
            try:
                sku = SKU.objects.get(name = root.attrib['Name'])
            except:
                messages.error(request, 'These keys are for a SKU that does not exist')
                return redirect('keys:product-list')

            # Print the keys
            for key in root:
                # Only add key if key doesn't already exist.
                try:
                    Key.objects.get(sku = sku, key = key.text)
                except:
                    k = Key(
                        key = key.text,
                        key_type = key.attrib['Type'],
                        imported_by = request.user,
                        imported_at = timezone.now(),
                        sku = sku
                    )
                    k.save()
                    print "Added key: %s" % k
                else:
                    print "Key already existed: %s" % key.text

            messages.success(request, "Keys added successfully.")
        else:
            messages.error(request, 'The file you selected is not a valid MSDNAA key file.')

    return redirect('keys:product-list')


class KeyList(KeydistListView):
    model = Key
    template_name = 'keys/list.html'

class SKUAdd(KeydistCreateView):
    model = SKU
    success_url = reverse_lazy('keys:product-list')

class ProductAdd(KeydistCreateView):
    model = Product
    success_url = reverse_lazy('keys:product-list')

class ProductDetail(KeydistDetailView):
    model = Product
    template_name = 'keys/products/detail.html'

class ProductList(KeydistListView):
    model = Product
    template_name = 'keys/products/list.html'

class ProductDelete(KeydistDeleteView):
    model = Product
    success_url = reverse_lazy('keys:product-list')

def allocate(request):
    if request.method == 'POST':
        form = forms.AllocateForm(request.POST)
        if form.is_valid():
            # Check if a user has already been allocated a key.
            old_keys = Key.objects.filter(
                sku = form.cleaned_data['SKU'],
                allocated_to = form.cleaned_data['user']
            )

            if old_keys:
                messages.error(request, "The user has already been allocated a key for this SKU. You are now being shown the existing allocation.")
                return redirect(old_keys[0].get_absolute_url())
            
            candidates = Key.objects.filter(
                sku = form.cleaned_data['SKU'],
                allocated_to = None
            )

            if not candidates:
                messages.error(request, "There are no unallocated keys left for this SKU.")
            else:
                key = candidates[0]
                key.allocated_to = form.cleaned_data['user']
                key.allocated_at = timezone.now()
                key.allocated_by = request.user
                key.save()

                return redirect('key:detail', key.id)
                messages.success(request, "A key has been allocated to the user.")

    return render(request, 'keys/allocate.html', {
        'form': forms.AllocateForm()
    })

def email(request, key_id):
    if request.method == 'POST':
        key = get_object_or_404(Key, pk = key_id)

        if not key.allocated_to:
            messages.error(request, 'This key has not been allocated to anybody, so we cannot send an email.')
            return redirect('keys:detail', key_id)

        message = """\
                Dear %s,

                %s has allocated you a key for '%s' on keydist.

                The key is as follows:

                %s

                --
                keydist
                http://keydist.comssa.org.au/
                """ % (key.allocated_to.first_name, request.user.first_name, key.sku.name, key.key)

        send_mail(
            subject = "%s, here's your key for %s" % (key.allocated_to.first_name, key.sku.name),
            message = dedent(message),
            from_email = 'keydist@comssa.org.au',
            recipient_list = (key.allocated_to.email,),
        )

        messages.success(request, "%s's key has been emailed to them." % key.allocated_to.first_name)
    else:
        messages.error(request, "Stop being sneaky...")
    return redirect('keys:detail', key_id)

class KeyDetail(KeydistDetailView):
    model = Key
    template_name = 'keys/detail.html'