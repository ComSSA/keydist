from django.shortcuts import render, redirect
from keys.models import *
from keydist.views import *
from django.contrib import messages
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