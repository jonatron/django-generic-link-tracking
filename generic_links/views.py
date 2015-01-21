from django.shortcuts import render, redirect

def generic_link_click(request, quick_id):
    id = numconv.str2int(quick_id.upper(), 32, numconv.BASE32)

    try:
        gl = GenericLink.objects.get(pk=id)
    except:
        raise Http404

    if gl.rotate:
        other_ids = gl.rotate.split(",")
        count = len(other_ids) + 1
        link_idx = randint(0, count - 1)
        if link_idx > 0:
            try:
                gl = GenericLink.objects.get(pk=other_ids[link_idx - 1])
            except gl.DoesNotExist:
                pass

    glc = GenericLinkClick()
    glc.link = gl
    glc.ip = get_ip(request)
    glc.save()

    return redirect(gl.url)