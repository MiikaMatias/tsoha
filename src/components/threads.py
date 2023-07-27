
def get_thread_header_element(base_url, thread_id):
    return f"""
            <p>
                <a href="{base_url}/threads/{thread_id}">
                    {thread_id}
                </a>
            </p>\n
"""

def get_threads(base_url, thread_ids):
    threads_returned = "<p>"

    for thread_id in thread_ids:
        threads_returned += get_thread_header_element(base_url, thread_id)

    threads_returned += "</p>"

    print(threads_returned)

    return threads_returned
