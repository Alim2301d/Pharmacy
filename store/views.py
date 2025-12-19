from django.shortcuts import redirect, render
from .models import Medicines
# Create your views here.
def home(request):
    med = Medicines.objects.all()
    context = {'med':med}
    return render(request,"index.html", context)

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10 , decimal_places=2)
    image = models.ImageField(upload_to='images/',null=True)
      
def add_prod(request):
    if request.method == 'POST':
        name = request.POST.get('m_name')
        description =request.POST.get('m_dec')
        price = request.POST.get('m_price')
        image = request.POST.get('m_img')

        Medicines.objects.create(
            name = name,
            description = description,
            price = price,
            image = image,
        )

        return redirect('home')

    return render(request, 'add_product.html')