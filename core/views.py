from django.shortcuts import render
from django.db.models import Q
from . import models
from fpdf import FPDF
from django.http import HttpResponse
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa  


# Create your views here.

def index(request):
    # q=request.GET.get("q") if request.GET.get('q') !=None else ''
    # job=models.Job.objects.filter(
    #     Q(job_name__icontains=q)
    # )
    job=models.Job.objects.all()
    count=job.count()
    # details=CompanyDetails.objects.all()
    # location=Location.objects.all()
    context={
        "job":job,
        #  "details":details,
        #  "location":location,
         "count":count
    }
    # print(q)
    # return render(request,"base/index.html",context)

    return render(request, 'core/index.html',context)




def searchJobView(request):
    q=request.GET.get("q") if request.GET.get('q') !=None else ''
    # searchedJob = models.Job.objects.get(Q(job_name__icontains=q))
    job=models.Job.objects.all()
    matchedJob=False
    
    try:
        matchedJob=True
        searchedJob = models.Job.objects.filter(Q(job_name__icontains=q))

    except searchedJob.DoesNotExist:
        matchedJob=False
        searchedJob=None
    

    count=searchedJob.count()

    context={
        "count":count,
        "searchedJob": searchedJob,
        "job":job,
    }
    return  render(request, 'core/index.html', context)


def jobDetailReportView(request,pk):
    job=models.Job.objects.get(pk=pk)
    jobname=job.job_name
    jobDescription=job.job_description
    jobResponsibility=job.job_responsibilities
    jobRequirement=job.job_requirements

    pdf=FPDF('P','mm','A4')
    pdf.add_page()
    pdf.set_font('courier','U',16)
    # pdf.cell(40,10,jobname)
    # pdf.set_font('courier', 'B', 16)
    # pdf.cell(40, 10, 'Job Description',0,1)
    # pdf.set_font('courier', '', 16)
    # pdf.cell(40, 10, jobDescription,0,1)
    # pdf.cell(40,40,jobRequirement)
    pdf.cell(0, 10, txt=f"Name: {jobname}", ln=True)
    pdf.cell(0, 10, txt=f"Name: {jobRequirement}", ln=True)



    filname=f'{jobname}.pdf'
    pdf.output(filname,'F')

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="dynamic.pdf"'
    pdf.output(response)

    return response


def render_to_pdf(template_src, context_dict={}):
     template = get_template('core/report.html')
     html  = template.render(context_dict)
     result = BytesIO()
 
     #This part will create the pdf.
     pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
     if not pdf.err:
         return HttpResponse(result.getvalue(), content_type='application/pdf')
     return None