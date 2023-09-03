import base64

def make_image_readable_thread(result):
    modified_result = []
    for row in result:
        thread_id, owner_id, image_id, title, created_at, content, username, image_data = row
        image_data_base64 = base64.b64encode(image_data).decode("utf-8")
        
        thread_dict = {
            'id': thread_id,
            'owner_id': owner_id,
            'image_id': image_id,
            'title': title,
            'created_at': created_at,
            'content': content,
            'username': username,
            'image_data_base64': image_data_base64
        }
        
        modified_result.append(thread_dict)

    return modified_result  

def make_image_readable_message(result):
    modified_result = []
    for row in result:
        thread_id, owner_id, image_id, created_at, content, username, image_data = row
        image_data_base64 = base64.b64encode(image_data).decode("utf-8")
        
        thread_dict = {
            'id': thread_id,
            'owner_id': owner_id,
            'image_id': image_id,
            'created_at': created_at,
            'content': content,
            'username': username,
            'image_data_base64': image_data_base64
        }
        
        modified_result.append(thread_dict)

    return modified_result  
