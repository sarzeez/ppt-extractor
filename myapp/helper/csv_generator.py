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
            actions_with_period = [action.strip() + '.' if not action.strip().endswith('.') else action.strip() for action in event['actions']]
            actions_str = ' '.join(actions_with_period)
            csv_writer.writerow([slide['title'], event['title'], actions_str])
    
    # Reset the StringIO object pointer
    csv_buffer.seek(0)

    response = HttpResponse(csv_buffer, content_type='text/csv')
    content_disposition = "attachment; filename=" + filename + ".csv"
    response['Content-Disposition'] = content_disposition
    return response
