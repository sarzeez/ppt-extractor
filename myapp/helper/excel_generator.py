import io
from django.http import HttpResponse
from openpyxl import Workbook

def generate_excel(data, filename):
    wb = Workbook()
    ws = wb.active

    # Write headers
    ws.append(['Concept Name', 'Attraction Title', 'Attraction Text'])

    # Write data
    for slide in data:
        for event in slide['events']:
            actions_str = '\n'.join(event['actions'])
            ws.append([slide['title'], event['title'], actions_str])

    # Save the workbook to a BytesIO object
    excel_buffer = io.BytesIO()
    wb.save(excel_buffer)
    excel_buffer.seek(0)

    response = HttpResponse(excel_buffer, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    content_disposition = "attachment; filename=" + filename + ".xlsx"
    response['Content-Disposition'] = content_disposition
    return response

def generate_concept_excel(data, filename):
    wb = Workbook()
    ws = wb.active

    # Write headers
    ws.append(['Concept Name', 'Concept Overview'])

    # Write data
    for slide in data:
        description_str = '\n'.join(slide['description'])
        ws.append([slide['name'], description_str])

    # Save the workbook to a BytesIO object
    excel_buffer = io.BytesIO()
    wb.save(excel_buffer)
    excel_buffer.seek(0)

    response = HttpResponse(excel_buffer, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    content_disposition = "attachment; filename=" + filename + ".xlsx"
    response['Content-Disposition'] = content_disposition
    return response
