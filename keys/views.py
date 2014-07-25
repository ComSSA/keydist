from django.shortcuts import render, redirect
from keys.models import *
from keydist.views import *
from django.contrib import messages
from django.utils import timezone
import xml.etree.ElementTree as ET
import forms

class KeyList(KeydistListView):
    model = Key
    template_name = 'keys/list.html'

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
                return redirect('keys:list')

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

    return redirect('keys:list')

class SKUAdd(KeydistCreateView):
    model = SKU

class ProductAdd(KeydistCreateView):
    model = Product

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
                return "FIXME"
            
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

                messages.success(request, "A key has been allocated to the user.")

    return render(request, 'keys/allocate.html', {
        'form': forms.AllocateForm()
    })

class KeyDetail(KeydistDetailView):
    model = Key
    template_name = 'keys/detail.html'