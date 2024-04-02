from pptx import Presentation


def extract_text_from_ppt_1(ppt_file):
    presentation = Presentation(ppt_file)
    slides_data = []

    for slide in presentation.slides:
        slide_data = {}
        slide_data['title'] = slide.shapes[0].text if slide.shapes[0].has_text_frame else None
        slide_data['events'] = []

        for shape in slide.shapes:
            if hasattr(shape, "text") and shape != slide.shapes[0]:
                actions = shape.text.split('\n')
                event_title = actions.pop(0).strip()
                event_actions = [action.strip() for action in actions if action.strip()]
                slide_data['events'].append({'title': event_title, 'actions': event_actions})

        slides_data.append(slide_data)

    return slides_data

def extract_text_from_ppt_2(ppt_file):
    presentation = Presentation(ppt_file)
    slides_data = []

    for slide in presentation.slides:
        slide_data = {}
        events_text = []
        for shape in slide.shapes:
            if hasattr(shape, "text") and shape.text.strip():
                if not slide_data:
                    slide_data["title"] = shape.text
                else:
                    events_text.append(shape.text)
        if events_text:
            events = '\n'.join(events_text)
            actions = events.split('\n')
            event_title = actions.pop(0).strip()
            slide_data["events"] = { 'title': event_title, 'actions': actions }
            slides_data.append(slide_data)

    return slides_data

