import csv
import io

from django.http import HttpResponse

def generate_csv(data, filename):
    # Create a StringIO object to store CSV data
    csv_buffer = io.StringIO()
    
    # Create a CSV writer
    csv_writer = csv.writer(csv_buffer)
    
    # Write headers
    csv_writer.writerow(['Concept Name', 'Attraction Title', 'Attraction Text'])
    
    # Write data
    for slide in data:
        for event in slide['events']:
            actions_str = '\n'.join(event['actions'])
            csv_writer.writerow([slide['title'], event['title'], f'{actions_str}'])
    
    # Reset the StringIO object pointer
    csv_buffer.seek(0)

    response = HttpResponse(csv_buffer, content_type='text/csv')
    content_disposition = "attachment; filename=" + filename + ".csv"
    response['Content-Disposition'] = content_disposition
    return response

def generate_concept_csv(data, filename):
    # Create a StringIO object to store CSV data
    csv_buffer = io.StringIO()
    
    # Create a CSV writer
    csv_writer = csv.writer(csv_buffer)
    
    # Write headers
    csv_writer.writerow(['Concept Name', 'Concept Overview'])
    
    # Write data
    for slide in data:
        description_str = '\n'.join(slide['description'])
        csv_writer.writerow([slide['name'], f'{description_str}'])
    
    # Reset the StringIO object pointer
    csv_buffer.seek(0)

    response = HttpResponse(csv_buffer, content_type='text/csv')
    content_disposition = "attachment; filename=" + filename + ".csv"
    response['Content-Disposition'] = content_disposition
    return response

def generate_module_csv(data, filename):
    # Create a StringIO object to store CSV data
    csv_buffer = io.StringIO()
    
    # Create a CSV writer
    csv_writer = csv.writer(csv_buffer)
    
    # Write headers
    csv_writer.writerow(['Section Name', 'Introduction Text'])
    
    # Write data
    for slide in data:
        description_str = '\n'.join(slide['description'])
        csv_writer.writerow([slide['name'], f'{description_str}'])
    
    # Reset the StringIO object pointer
    csv_buffer.seek(0)

    response = HttpResponse(csv_buffer, content_type='text/csv')
    content_disposition = "attachment; filename=" + filename + ".csv"
    response['Content-Disposition'] = content_disposition
    return response
