from django.shortcuts import render


def index(request):
    # どこかで保存
    request.session['user_id'] = 1  # User.objects.get(pk=1).id

    # 取得
    user_id = request.session.get('user_id', '')

    return render(request, 'index.html', {
        'context1': 'hello1 message',
        'user_id': user_id,
    })