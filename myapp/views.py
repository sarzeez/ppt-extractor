from django.shortcuts import redirect, render

from .helper.excel_generator import generate_excel, generate_concept_excel
from .helper.csv_generator import generate_csv, generate_concept_csv 
from .helper.ppt_extractors import extract_text_from_ppt_1, extract_text_from_ppt_2, extract_text_from_ppt_3


# Create your views here.
def home(request):
    if request.method == 'POST' and request.FILES:
        selected_format = request.POST.get('format')
        selected_type = request.POST.get('type')
        uploaded_file = request.FILES['uploaded_file']
        filename = uploaded_file.name.split('.')[0]

        format_type = selected_format + "_" + selected_type
        
        match format_type:
            case "format1_csv":
                return generate_csv(extract_text_from_ppt_1(uploaded_file), filename)
            case "format1_xlsx":
                return generate_excel(extract_text_from_ppt_1(uploaded_file), filename)
            case "format2_csv":
                return generate_csv(extract_text_from_ppt_2(uploaded_file), filename)
            case "format2_xlsx":
                return generate_excel(extract_text_from_ppt_2(uploaded_file), filename)
            case "concept_csv":
                return generate_concept_csv(extract_text_from_ppt_3(uploaded_file), filename)
            case "concept_xlsx":
                return generate_concept_excel(extract_text_from_ppt_3(uploaded_file), filename)
            case _:
                return redirect('home')
    return render(request, 'home.html', {})


