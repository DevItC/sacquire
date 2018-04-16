import facebook
from rq import Queue
from rq.job import Job
from worker import conn
from flask import Flask, render_template, request, send_file, jsonify, redirect, url_for
import time

app = Flask(__name__)
q = Queue(connection=conn)


@app.route('/home', methods=['GET'])
def index():
    # image = request.args.get('image')
    preview_link = request.args.get('preview_link')
    link = request.args.get('link')
    return render_template('form.html', preview_link=preview_link, link=link )

@app.route('/')
def index2():
    return redirect(url_for('index', preview_link="", link=""))

@app.route('/enqueue', methods=['POST'])
def enqueue():
    args = (request.form['URL'],)
    task = q.enqueue_call(func=facebook.give_links, args=args, result_ttl=5000, timeout=3600)
    
    response = {
        'status': 'success',
        'data': {
            'task_id': task.get_id()
        }
    }
    return jsonify(response), 202


@app.route('/tasks/<task_id>', methods=['GET'])
def get_status(task_id):
    task = q.fetch_job(task_id)
    if task:
        status = task.get_status()
        response = {
            'status': 'success',
            'data': {
                'task_id': task.get_id(),
                'task_status': task.get_status(),
            }
        }
        if (status=='finished'):
            result = q.fetch_job(task_id).result
            response['data']['preview_link'] = result[0][1]
            response['data']['link'] = result[1][1]
    else:
        response = {'status': 'error'}

    return jsonify(response)


# @app.route('/download/<task_id>', methods=['GET'])
# def preview(task_id):
#     result = q.fetch_job(task_id).result
#     if result:
#         response = {
#             'image' : True,
#             'preview_link' : result[0][1],
#             'link' : result[1][1],
#         }
#     # return redirect(url_for('index', image=True, preview_link=result[0][1], link=result[1][1]))
#     return jsonify(response)

# @app.route('/download/<task_id>', methods=['GET'])
# def download(task_id):
#     task = q.fetch_job(task_id)
#     print (task.result)
#     return send_file(task.result, as_attachment=True)



if __name__=='__main__':
    app.run()
