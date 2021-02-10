from django.shortcuts import render

def index(request):
	syear = ['2021-22','2020-21','2019-20','2018-19','2017-18','2016-17']
	taxpayer = ['Individual','HUF',"Domestic Company",'Foreign Company','Firms','Corporate Society']
	category = ['Male','Female','Senior Citizen','Super Senior Citizen']
	status =['Resident','NRI',]
	if request.method=='POST':
		ty = request.POST['year']
		tp = request.POST['taxpayer']
		cat = request.POST['category']
		stat = request.POST['status']
		annincome = request.POST['income']
		

		if request.POST.get('txtsub'):
			ain = float(annincome)

			if ain >250000:
				x = 'From income 2,50,001 - Rs 5,00,000. TAX RATE IS 5%'
				y = 'From income 5,00,001 - Rs 7,50,000. TAX RATE IS 10%'
				z = 'From income 7,50,001 - Rs 10,00,000. TAX RATE IS 15%'
				a = 'From income 10,00,001 - Rs 12,50,000. TAX RATE IS 20%'
				d =	'From income 12,50,001 - Rs 15,00,000. TAX RATE IS 25%'
				b = 'Above 15,00,000. TAX RATE IS 30%'

				if ain >250000 and ain <= 500000:
					net = ain - 250000
					pay = net * 0.05
					amtpay = "%0.2f"%pay
				elif ain > 500000 and ain <= 750000:
					net = ain - 500000
					pay = 12500 + ( net * 0.1)
					amtpay = "%0.2f"%pay
				elif ain > 750000 and ain <= 1000000:
					net = ain - 750000
					pay = 37500 + (net * 0.15)
					amtpay = "%0.2f"%pay
				elif ain > 1000000 and ain <= 1250000:
					net = ain - 1000000
					pay = 75000 + (net * 0.2)
					amtpay = "%0.2f"%pay
				elif ain > 1250000 and ain <= 1500000:
					net = ain - 1250000
					pay = 125000 + (net * 0.25)
					amtpay = "%0.2f"%pay
				elif ain > 1500000:
					net = ain - 1500000
					pay = 187500 + (net * 0.3)
					amtpay = "%0.2f"%pay
						

				return render(request,'taxcalculator/form.html',{'year':syear, 'taxpayer':taxpayer,'category':category,'status':status,"x":x,"y":y,"z":z,"a":a,"b":b,'ty':ty,'tp':tp,'cat':cat,'stat':stat,"annincome":annincome,"d":d ,"amtpay":"Tax payable = "+ str(amtpay)})
			else:
				c = "Your income is not taxable"
				return render(request,'taxcalculator/form.html',{'year':syear, 'taxpayer':taxpayer,'category':category,'status':status,"c":c,'ty':ty,'tp':tp,'cat':cat,'stat':stat,"annincome":annincome})
		else:
			return render(request,'taxcalculator/form.html',{'year':syear, 'taxpayer':taxpayer,'category':category,'status':status})

	return render(request,'taxcalculator/form.html',{'year':syear, 'taxpayer':taxpayer,'category':category,'status':status})