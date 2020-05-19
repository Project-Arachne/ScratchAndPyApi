from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers([u'parseCookie', u'fs', u'WebSocket', u'SESSION_FILE', u'request', u'crypto', u'requestJSON', u'SERVER', u'util', u'CLOUD_SERVER', u'https', u'Scratch', u'API_SERVER', u'net', u'PROJECTS_SERVER', u'events', u'CDN_SERVER'])
@Js
def PyJsHoisted_parseCookie_(cookie, this, arguments, var=var):
    var = Scope({u'this':this, u'cookie':cookie, u'arguments':arguments}, var)
    var.registers([u'i', u'pair', u'cookies', u'cookie', u'each'])
    PyJs_Object_6_ = Js({})
    var.put(u'cookies', PyJs_Object_6_)
    var.put(u'each', var.get(u'cookie').callprop(u'split', Js(u';')))
    var.put(u'i', var.get(u'each').get(u'length'))
    while (var.put(u'i',Js(var.get(u'i').to_number())-Js(1))+Js(1)):
        if PyJsStrictEq(var.get(u'each').get(var.get(u'i')).callprop(u'indexOf', Js(u'=')),(-Js(1.0))):
            continue
        var.put(u'pair', var.get(u'each').get(var.get(u'i')).callprop(u'split', Js(u'=')))
        var.get(u'cookies').put(var.get(u'pair').get(u'0').callprop(u'trim'), var.get(u'pair').get(u'1').callprop(u'trim'))
    return var.get(u'cookies')
PyJsHoisted_parseCookie_.func_name = u'parseCookie'
var.put(u'parseCookie', PyJsHoisted_parseCookie_)
@Js
def PyJsHoisted_request_(options, cb, this, arguments, var=var):
    var = Scope({u'this':this, u'cb':cb, u'options':options, u'arguments':arguments}, var)
    var.registers([u'headers', u'req', u'cb', u'name', u'options'])
    PyJs_Object_0_ = Js({u'Cookie':Js(u'scratchcsrftoken=a; scratchlanguage=en;'),u'X-CSRFToken':Js(u'a'),u'referer':Js(u'https://scratch.mit.edu')})
    var.put(u'headers', PyJs_Object_0_)
    if var.get(u'options').get(u'headers'):
        for PyJsTemp in var.get(u'options').get(u'headers'):
            var.put(u'name', PyJsTemp)
            var.get(u'headers').put(var.get(u'name'), var.get(u'options').get(u'headers').get(var.get(u'name')))
    if var.get(u'options').get(u'body'):
        var.get(u'headers').put(u'Content-Length', var.get(u'Buffer').callprop(u'byteLength', var.get(u'options').get(u'body')))
    if var.get(u'options').get(u'sessionId'):
        var.get(u'headers').put(u'Cookie', ((Js(u'scratchsessionsid=')+var.get(u'options').get(u'sessionId'))+Js(u';')), u'+')
    PyJs_Object_1_ = Js({u'hostname':(var.get(u'options').get(u'hostname') or var.get(u'SERVER')),u'port':Js(443.0),u'path':var.get(u'options').get(u'path'),u'method':(var.get(u'options').get(u'method') or Js(u'GET')),u'headers':var.get(u'headers')})
    @Js
    def PyJs_anonymous_2_(response, this, arguments, var=var):
        var = Scope({u'this':this, u'response':response, u'arguments':arguments}, var)
        var.registers([u'parts', u'response'])
        var.put(u'parts', Js([]))
        @Js
        def PyJs_anonymous_3_(chunk, this, arguments, var=var):
            var = Scope({u'this':this, u'chunk':chunk, u'arguments':arguments}, var)
            var.registers([u'chunk'])
            var.get(u'parts').callprop(u'push', var.get(u'chunk'))
        PyJs_anonymous_3_._set_name(u'anonymous')
        var.get(u'response').callprop(u'on', Js(u'data'), PyJs_anonymous_3_)
        @Js
        def PyJs_anonymous_4_(this, arguments, var=var):
            var = Scope({u'this':this, u'arguments':arguments}, var)
            var.registers([])
            var.get(u'cb')(var.get(u"null"), var.get(u'Buffer').callprop(u'concat', var.get(u'parts')).callprop(u'toString'), var.get(u'response'))
        PyJs_anonymous_4_._set_name(u'anonymous')
        var.get(u'response').callprop(u'on', Js(u'end'), PyJs_anonymous_4_)
    PyJs_anonymous_2_._set_name(u'anonymous')
    var.put(u'req', var.get(u'https').callprop(u'request', PyJs_Object_1_, PyJs_anonymous_2_))
    var.get(u'req').callprop(u'on', Js(u'error'), var.get(u'cb'))
    if var.get(u'options').get(u'body'):
        var.get(u'req').callprop(u'write', var.get(u'options').get(u'body'))
    var.get(u'req').callprop(u'end')
PyJsHoisted_request_.func_name = u'request'
var.put(u'request', PyJsHoisted_request_)
@Js
def PyJsHoisted_requestJSON_(options, cb, this, arguments, var=var):
    var = Scope({u'this':this, u'cb':cb, u'options':options, u'arguments':arguments}, var)
    var.registers([u'cb', u'options'])
    @Js
    def PyJs_anonymous_5_(err, body, response, this, arguments, var=var):
        var = Scope({u'body':body, u'this':this, u'response':response, u'err':err, u'arguments':arguments}, var)
        var.registers([u'body', u'response', u'err'])
        if var.get(u'err'):
            return var.get(u'cb')(var.get(u'err'))
        try:
            var.get(u'cb')(var.get(u"null"), var.get(u'JSON').callprop(u'parse', var.get(u'body')))
        except PyJsException as PyJsTempException:
            PyJsHolder_65_42748641 = var.own.get(u'e')
            var.force_own_put(u'e', PyExceptionToJs(PyJsTempException))
            try:
                var.get(u'cb')(var.get(u'e'))
            finally:
                if PyJsHolder_65_42748641 is not None:
                    var.own[u'e'] = PyJsHolder_65_42748641
                else:
                    del var.own[u'e']
                del PyJsHolder_65_42748641
    PyJs_anonymous_5_._set_name(u'anonymous')
    var.get(u'request')(var.get(u'options'), PyJs_anonymous_5_)
PyJsHoisted_requestJSON_.func_name = u'requestJSON'
var.put(u'requestJSON', PyJsHoisted_requestJSON_)
var.put(u'https', var.get(u'require')(Js(u'https')))
var.put(u'net', var.get(u'require')(Js(u'net')))
var.put(u'util', var.get(u'require')(Js(u'util')))
var.put(u'events', var.get(u'require')(Js(u'events')))
var.put(u'crypto', var.get(u'require')(Js(u'crypto')))
var.put(u'fs', var.get(u'require')(Js(u'fs')))
var.put(u'WebSocket', var.get(u'require')(Js(u'ws')))
var.put(u'SERVER', Js(u'scratch.mit.edu'))
var.put(u'PROJECTS_SERVER', Js(u'projects.scratch.mit.edu'))
var.put(u'CDN_SERVER', Js(u'cdn.scratch.mit.edu'))
var.put(u'CLOUD_SERVER', Js(u'clouddata.scratch.mit.edu'))
var.put(u'API_SERVER', Js(u'api.scratch.mit.edu'))
var.put(u'SESSION_FILE', Js(u'.scratchSession'))
pass
pass
pass
PyJs_Object_7_ = Js({})
var.put(u'Scratch', PyJs_Object_7_)
@Js
def PyJs_anonymous_8_(projectId, cb, this, arguments, var=var):
    var = Scope({u'this':this, u'projectId':projectId, u'arguments':arguments, u'cb':cb}, var)
    var.registers([u'projectId', u'cb'])
    PyJs_Object_9_ = Js({u'hostname':var.get(u'PROJECTS_SERVER'),u'path':(Js(u'/')+var.get(u'projectId')),u'method':Js(u'GET')})
    var.get(u'requestJSON')(PyJs_Object_9_, var.get(u'cb'))
PyJs_anonymous_8_._set_name(u'anonymous')
var.get(u'Scratch').put(u'getProject', PyJs_anonymous_8_)
@Js
def PyJs_anonymous_10_(username, cb, this, arguments, var=var):
    var = Scope({u'username':username, u'cb':cb, u'this':this, u'arguments':arguments}, var)
    var.registers([u'username', u'cb'])
    PyJs_Object_11_ = Js({u'hostname':var.get(u'API_SERVER'),u'path':((Js(u'/users/')+var.get(u'username'))+Js(u'/projects')),u'method':Js(u'GET')})
    var.get(u'requestJSON')(PyJs_Object_11_, var.get(u'cb'))
PyJs_anonymous_10_._set_name(u'anonymous')
var.get(u'Scratch').put(u'getProjects', PyJs_anonymous_10_)
@Js
def PyJs_anonymous_12_(username, id, sessionId, this, arguments, var=var):
    var = Scope({u'username':username, u'this':this, u'sessionId':sessionId, u'id':id, u'arguments':arguments}, var)
    var.registers([u'username', u'sessionId', u'id'])
    var.get(u"this").put(u'username', var.get(u'username'))
    var.get(u"this").put(u'id', var.get(u'id'))
    var.get(u"this").put(u'sessionId', var.get(u'sessionId'))
PyJs_anonymous_12_._set_name(u'anonymous')
var.get(u'Scratch').put(u'UserSession', PyJs_anonymous_12_)
@Js
def PyJs_anonymous_13_(username, password, cb, this, arguments, var=var):
    var = Scope({u'username':username, u'cb':cb, u'password':password, u'this':this, u'arguments':arguments}, var)
    var.registers([u'username', u'cb', u'password'])
    PyJs_Object_15_ = Js({u'username':var.get(u'username'),u'password':var.get(u'password')})
    PyJs_Object_16_ = Js({u'X-Requested-With':Js(u'XMLHttpRequest')})
    PyJs_Object_14_ = Js({u'path':Js(u'/login/'),u'method':Js(u'POST'),u'body':var.get(u'JSON').callprop(u'stringify', PyJs_Object_15_),u'headers':PyJs_Object_16_})
    @Js
    def PyJs_anonymous_17_(err, body, response, this, arguments, var=var):
        var = Scope({u'body':body, u'this':this, u'response':response, u'err':err, u'arguments':arguments}, var)
        var.registers([u'body', u'user', u'err', u'response'])
        if var.get(u'err'):
            return var.get(u'cb')(var.get(u'err'))
        try:
            var.put(u'user', var.get(u'JSON').callprop(u'parse', var.get(u'body')).get(u'0'))
            if var.get(u'user').get(u'msg'):
                return var.get(u'cb')(var.get(u'Error').create(var.get(u'user').get(u'msg')))
            var.get(u'cb')(var.get(u"null"), var.get(u'Scratch').get(u'UserSession').create(var.get(u'user').get(u'username'), var.get(u'user').get(u'id'), var.get(u'parseCookie')(var.get(u'response').get(u'headers').get(u'set-cookie').get(u'0')).get(u'scratchsessionsid')))
        except PyJsException as PyJsTempException:
            PyJsHolder_65_25275271 = var.own.get(u'e')
            var.force_own_put(u'e', PyExceptionToJs(PyJsTempException))
            try:
                var.get(u'cb')(var.get(u'e'))
            finally:
                if PyJsHolder_65_25275271 is not None:
                    var.own[u'e'] = PyJsHolder_65_25275271
                else:
                    del var.own[u'e']
                del PyJsHolder_65_25275271
    PyJs_anonymous_17_._set_name(u'anonymous')
    var.get(u'request')(PyJs_Object_14_, PyJs_anonymous_17_)
PyJs_anonymous_13_._set_name(u'anonymous')
var.get(u'Scratch').get(u'UserSession').put(u'create', PyJs_anonymous_13_)
@Js
def PyJs_anonymous_18_(cb, this, arguments, var=var):
    var = Scope({u'this':this, u'cb':cb, u'arguments':arguments}, var)
    var.registers([u'cb', u'prompt'])
    var.put(u'prompt', var.get(u'require')(Js(u'prompt')))
    var.get(u'prompt').callprop(u'start')
    PyJs_Object_19_ = Js({u'name':Js(u'username')})
    PyJs_Object_20_ = Js({u'name':Js(u'password'),u'hidden':var.get(u'true')})
    @Js
    def PyJs_anonymous_21_(err, results, this, arguments, var=var):
        var = Scope({u'this':this, u'results':results, u'err':err, u'arguments':arguments}, var)
        var.registers([u'results', u'err'])
        if var.get(u'err'):
            return var.get(u'cb')(var.get(u'err'))
        var.get(u'Scratch').get(u'UserSession').callprop(u'create', var.get(u'results').get(u'username'), var.get(u'results').get(u'password'), var.get(u'cb'))
    PyJs_anonymous_21_._set_name(u'anonymous')
    var.get(u'prompt').callprop(u'get', Js([PyJs_Object_19_, PyJs_Object_20_]), PyJs_anonymous_21_)
PyJs_anonymous_18_._set_name(u'anonymous')
var.get(u'Scratch').get(u'UserSession').put(u'prompt', PyJs_anonymous_18_)
@Js
def PyJs_anonymous_22_(cb, this, arguments, var=var):
    var = Scope({u'this':this, u'cb':cb, u'arguments':arguments}, var)
    var.registers([u'cb', u'prompt'])
    @Js
    def PyJsHoisted_prompt_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([])
        @Js
        def PyJs_anonymous_23_(err, session, this, arguments, var=var):
            var = Scope({u'this':this, u'session':session, u'arguments':arguments, u'err':err}, var)
            var.registers([u'session', u'err'])
            if var.get(u'err'):
                return var.get(u'cb')(var.get(u'err'))
            @Js
            def PyJs_anonymous_24_(this, arguments, var=var):
                var = Scope({u'this':this, u'arguments':arguments}, var)
                var.registers([])
                var.get(u'cb')(var.get(u"null"), var.get(u'session'))
            PyJs_anonymous_24_._set_name(u'anonymous')
            var.get(u'session').callprop(u'_saveSession', PyJs_anonymous_24_)
        PyJs_anonymous_23_._set_name(u'anonymous')
        var.get(u'Scratch').get(u'UserSession').callprop(u'prompt', PyJs_anonymous_23_)
    PyJsHoisted_prompt_.func_name = u'prompt'
    var.put(u'prompt', PyJsHoisted_prompt_)
    pass
    @Js
    def PyJs_anonymous_25_(err, data, this, arguments, var=var):
        var = Scope({u'this':this, u'data':data, u'arguments':arguments, u'err':err}, var)
        var.registers([u'data', u'session', u'obj', u'err'])
        if var.get(u'err'):
            return var.get(u'prompt')()
        var.put(u'obj', var.get(u'JSON').callprop(u'parse', var.get(u'data').callprop(u'toString')))
        var.put(u'session', var.get(u'Scratch').get(u'UserSession').create(var.get(u'obj').get(u'username'), var.get(u'obj').get(u'id'), var.get(u'obj').get(u'sessionId')))
        @Js
        def PyJs_anonymous_26_(err, valid, this, arguments, var=var):
            var = Scope({u'this':this, u'valid':valid, u'arguments':arguments, u'err':err}, var)
            var.registers([u'valid', u'err'])
            if var.get(u'err'):
                return var.get(u'cb')(var.get(u'err'))
            if var.get(u'valid'):
                return var.get(u'cb')(var.get(u"null"), var.get(u'session'))
            var.get(u'prompt')()
        PyJs_anonymous_26_._set_name(u'anonymous')
        var.get(u'session').callprop(u'verify', PyJs_anonymous_26_)
    PyJs_anonymous_25_._set_name(u'anonymous')
    var.get(u'fs').callprop(u'readFile', var.get(u'SESSION_FILE'), PyJs_anonymous_25_)
PyJs_anonymous_22_._set_name(u'anonymous')
var.get(u'Scratch').get(u'UserSession').put(u'load', PyJs_anonymous_22_)
@Js
def PyJs_anonymous_27_(cb, this, arguments, var=var):
    var = Scope({u'this':this, u'cb':cb, u'arguments':arguments}, var)
    var.registers([u'cb'])
    PyJs_Object_28_ = Js({u'username':var.get(u"this").get(u'username'),u'id':var.get(u"this").get(u'id'),u'sessionId':var.get(u"this").get(u'sessionId')})
    var.get(u'fs').callprop(u'writeFile', var.get(u'SESSION_FILE'), var.get(u'JSON').callprop(u'stringify', PyJs_Object_28_), var.get(u'cb'))
PyJs_anonymous_27_._set_name(u'anonymous')
var.get(u'Scratch').get(u'UserSession').get(u'prototype').put(u'_saveSession', PyJs_anonymous_27_)
@Js
def PyJs_anonymous_29_(cb, this, arguments, var=var):
    var = Scope({u'this':this, u'cb':cb, u'arguments':arguments}, var)
    var.registers([u'cb'])
    PyJs_Object_30_ = Js({u'path':Js(u'/messages/ajax/get-message-count/'),u'sessionId':var.get(u"this").get(u'sessionId')})
    @Js
    def PyJs_anonymous_31_(err, body, response, this, arguments, var=var):
        var = Scope({u'body':body, u'this':this, u'response':response, u'err':err, u'arguments':arguments}, var)
        var.registers([u'body', u'response', u'err'])
        var.get(u'cb')(var.get(u"null"), (var.get(u'err').neg() and PyJsStrictEq(var.get(u'response').get(u'statusCode'),Js(200.0))))
    PyJs_anonymous_31_._set_name(u'anonymous')
    var.get(u'request')(PyJs_Object_30_, PyJs_anonymous_31_)
PyJs_anonymous_29_._set_name(u'anonymous')
var.get(u'Scratch').get(u'UserSession').get(u'prototype').put(u'verify', PyJs_anonymous_29_)
var.get(u'Scratch').get(u'UserSession').get(u'prototype').put(u'getProject', var.get(u'Scratch').get(u'getProject'))
@Js
def PyJs_anonymous_32_(cb, this, arguments, var=var):
    var = Scope({u'this':this, u'cb':cb, u'arguments':arguments}, var)
    var.registers([u'cb'])
    var.get(u'Scratch').callprop(u'getProjects', var.get(u"this").get(u'username'), var.get(u'cb'))
PyJs_anonymous_32_._set_name(u'anonymous')
var.get(u'Scratch').get(u'UserSession').get(u'prototype').put(u'getProjects', PyJs_anonymous_32_)
@Js
def PyJs_anonymous_33_(cb, this, arguments, var=var):
    var = Scope({u'this':this, u'cb':cb, u'arguments':arguments}, var)
    var.registers([u'cb'])
    PyJs_Object_34_ = Js({u'hostname':var.get(u'SERVER'),u'path':Js(u'/site-api/projects/all/'),u'method':Js(u'GET'),u'sessionId':var.get(u"this").get(u'sessionId')})
    var.get(u'requestJSON')(PyJs_Object_34_, var.get(u'cb'))
PyJs_anonymous_33_._set_name(u'anonymous')
var.get(u'Scratch').get(u'UserSession').get(u'prototype').put(u'getAllProjects', PyJs_anonymous_33_)
@Js
def PyJs_anonymous_35_(projectId, payload, cb, this, arguments, var=var):
    var = Scope({u'this':this, u'projectId':projectId, u'payload':payload, u'arguments':arguments, u'cb':cb}, var)
    var.registers([u'projectId', u'payload', u'cb'])
    if PyJsStrictNeq(var.get(u'payload',throw=False).typeof(),Js(u'string')):
        var.put(u'payload', var.get(u'JSON').callprop(u'stringify', var.get(u'payload')))
    PyJs_Object_36_ = Js({u'hostname':var.get(u'PROJECTS_SERVER'),u'path':((Js(u'/internalapi/project/')+var.get(u'projectId'))+Js(u'/set/')),u'method':Js(u'POST'),u'body':var.get(u'payload'),u'sessionId':var.get(u"this").get(u'sessionId')})
    var.get(u'requestJSON')(PyJs_Object_36_, var.get(u'cb'))
PyJs_anonymous_35_._set_name(u'anonymous')
var.get(u'Scratch').get(u'UserSession').get(u'prototype').put(u'setProject', PyJs_anonymous_35_)
@Js
def PyJs_anonymous_37_(cb, this, arguments, var=var):
    var = Scope({u'this':this, u'cb':cb, u'arguments':arguments}, var)
    var.registers([u'cb'])
    PyJs_Object_38_ = Js({u'hostname':var.get(u'SERVER'),u'path':((Js(u'/internalapi/backpack/')+var.get(u"this").get(u'username'))+Js(u'/get/')),u'method':Js(u'GET'),u'sessionId':var.get(u"this").get(u'sessionId')})
    var.get(u'requestJSON')(PyJs_Object_38_, var.get(u'cb'))
PyJs_anonymous_37_._set_name(u'anonymous')
var.get(u'Scratch').get(u'UserSession').get(u'prototype').put(u'getBackpack', PyJs_anonymous_37_)
@Js
def PyJs_anonymous_39_(payload, cb, this, arguments, var=var):
    var = Scope({u'this':this, u'cb':cb, u'payload':payload, u'arguments':arguments}, var)
    var.registers([u'cb', u'payload'])
    if PyJsStrictNeq(var.get(u'payload',throw=False).typeof(),Js(u'string')):
        var.put(u'payload', var.get(u'JSON').callprop(u'stringify', var.get(u'payload')))
    PyJs_Object_40_ = Js({u'hostname':var.get(u'SERVER'),u'path':((Js(u'/internalapi/backpack/')+var.get(u"this").get(u'username'))+Js(u'/set/')),u'method':Js(u'POST'),u'body':var.get(u'payload'),u'sessionId':var.get(u"this").get(u'sessionId')})
    var.get(u'requestJSON')(PyJs_Object_40_, var.get(u'cb'))
PyJs_anonymous_39_._set_name(u'anonymous')
var.get(u'Scratch').get(u'UserSession').get(u'prototype').put(u'setBackpack', PyJs_anonymous_39_)
@Js
def PyJs_anonymous_41_(options, cb, this, arguments, var=var):
    var = Scope({u'this':this, u'cb':cb, u'options':options, u'arguments':arguments}, var)
    var.registers([u'cb', u'type', u'id', u'options'])
    pass
    if var.get(u'options').get(u'project'):
        var.put(u'type', Js(u'project'))
        var.put(u'id', var.get(u'options').get(u'project'))
    else:
        if var.get(u'options').get(u'user'):
            var.put(u'type', Js(u'user'))
            var.put(u'id', var.get(u'options').get(u'user'))
        else:
            if var.get(u'options').get(u'studio'):
                var.put(u'type', Js(u'gallery'))
                var.put(u'id', var.get(u'options').get(u'studio'))
    PyJs_Object_43_ = Js({u'content':var.get(u'options').get(u'content'),u'parent_id':(var.get(u'options').get(u'parent') or Js(u'')),u'commentee_id':(var.get(u'options').get(u'replyto') or Js(u''))})
    PyJs_Object_42_ = Js({u'hostname':var.get(u'SERVER'),u'path':((((Js(u'/site-api/comments/')+var.get(u'type'))+Js(u'/'))+var.get(u'id'))+Js(u'/add/')),u'method':Js(u'POST'),u'body':var.get(u'JSON').callprop(u'stringify', PyJs_Object_43_),u'sessionId':var.get(u"this").get(u'sessionId')})
    var.get(u'request')(PyJs_Object_42_, var.get(u'cb'))
PyJs_anonymous_41_._set_name(u'anonymous')
var.get(u'Scratch').get(u'UserSession').get(u'prototype').put(u'addComment', PyJs_anonymous_41_)
@Js
def PyJs_anonymous_44_(projectId, cb, this, arguments, var=var):
    var = Scope({u'this':this, u'projectId':projectId, u'arguments':arguments, u'cb':cb}, var)
    var.registers([u'projectId', u'cb'])
    var.get(u'Scratch').get(u'CloudSession').callprop(u'_create', var.get(u"this"), var.get(u'projectId'), var.get(u'cb'))
PyJs_anonymous_44_._set_name(u'anonymous')
var.get(u'Scratch').get(u'UserSession').get(u'prototype').put(u'cloudSession', PyJs_anonymous_44_)
@Js
def PyJs_anonymous_45_(user, projectId, this, arguments, var=var):
    var = Scope({u'this':this, u'projectId':projectId, u'user':user, u'arguments':arguments}, var)
    var.registers([u'projectId', u'user'])
    var.get(u"this").put(u'user', var.get(u'user'))
    var.get(u"this").put(u'projectId', (Js(u'')+var.get(u'projectId')))
    var.get(u"this").put(u'connection', var.get(u"null"))
    var.get(u"this").put(u'attemptedPackets', Js([]))
    var.get(u"this").put(u'variables', var.get(u'Object').callprop(u'create', var.get(u"null")))
    var.get(u"this").put(u'_variables', var.get(u'Object').callprop(u'create', var.get(u"null")))
PyJs_anonymous_45_._set_name(u'anonymous')
var.get(u'Scratch').put(u'CloudSession', PyJs_anonymous_45_)
var.get(u'util').callprop(u'inherits', var.get(u'Scratch').get(u'CloudSession'), var.get(u'events').get(u'EventEmitter'))
@Js
def PyJs_anonymous_46_(user, projectId, cb, this, arguments, var=var):
    var = Scope({u'this':this, u'projectId':projectId, u'user':user, u'arguments':arguments, u'cb':cb}, var)
    var.registers([u'projectId', u'session', u'user', u'cb'])
    var.put(u'session', var.get(u'Scratch').get(u'CloudSession').create(var.get(u'user'), var.get(u'projectId')))
    @Js
    def PyJs_anonymous_47_(err, this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments, u'err':err}, var)
        var.registers([u'err'])
        if var.get(u'err'):
            return var.get(u'cb')(var.get(u'err'))
        var.get(u'cb')(var.get(u"null"), var.get(u'session'))
    PyJs_anonymous_47_._set_name(u'anonymous')
    var.get(u'session').callprop(u'_connect', PyJs_anonymous_47_)
PyJs_anonymous_46_._set_name(u'anonymous')
var.get(u'Scratch').get(u'CloudSession').put(u'_create', PyJs_anonymous_46_)
@Js
def PyJs_anonymous_48_(cb, this, arguments, var=var):
    var = Scope({u'this':this, u'cb':cb, u'arguments':arguments}, var)
    var.registers([u'cb', u'self', u'stream'])
    var.put(u'self', var.get(u"this"))
    PyJs_Object_50_ = Js({u'cookie':((Js(u'scratchsessionsid=')+var.get(u"this").get(u'user').get(u'sessionId'))+Js(u';')),u'origin':Js(u'https://scratch.mit.edu')})
    PyJs_Object_49_ = Js({u'headers':PyJs_Object_50_})
    var.get(u"this").put(u'connection', var.get(u'WebSocket').create(((Js(u'wss://')+var.get(u'CLOUD_SERVER'))+Js(u'/')), Js([]), PyJs_Object_49_))
    @Js
    def PyJs_anonymous_51_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'i'])
        var.get(u'self').callprop(u'_sendHandshake')
        #for JS loop
        var.put(u'i', Js(0.0))
        while (var.get(u'i')<var.get(u'self').get(u'attemptedPackets').get(u'length')):
            try:
                var.get(u'self').callprop(u'_sendPacket', var.get(u'self').get(u'attemptedPackets').get(var.get(u'i')))
            finally:
                    (var.put(u'i',Js(var.get(u'i').to_number())+Js(1))-Js(1))
        var.get(u'self').put(u'attemptedPackets', Js([]))
        if var.get(u'cb'):
            var.get(u'cb')()
    PyJs_anonymous_51_._set_name(u'anonymous')
    var.get(u"this").get(u'connection').callprop(u'on', Js(u'open'), PyJs_anonymous_51_)
    @Js
    def PyJs_anonymous_52_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([])
        var.get(u'self').callprop(u'_connect')
    PyJs_anonymous_52_._set_name(u'anonymous')
    var.get(u"this").get(u'connection').callprop(u'on', Js(u'close'), PyJs_anonymous_52_)
    var.put(u'stream', Js(u''))
    @Js
    def PyJs_anonymous_53_(chunk, this, arguments, var=var):
        var = Scope({u'this':this, u'chunk':chunk, u'arguments':arguments}, var)
        var.registers([u'i', u'line', u'packets', u'chunk', u'packet'])
        var.put(u'stream', var.get(u'chunk'), u'+')
        var.put(u'packets', var.get(u'stream').callprop(u'split', Js(u'\n')))
        #for JS loop
        var.put(u'i', Js(0.0))
        while (var.get(u'i')<(var.get(u'packets').get(u'length')-Js(1.0))):
            try:
                var.put(u'line', var.get(u'packets').get(var.get(u'i')))
                pass
                try:
                    var.put(u'packet', var.get(u'JSON').callprop(u'parse', var.get(u'line')))
                except PyJsException as PyJsTempException:
                    PyJsHolder_657272_68901310 = var.own.get(u'err')
                    var.force_own_put(u'err', PyExceptionToJs(PyJsTempException))
                    try:
                        var.get(u'console').callprop(u'warn', Js(u'Invalid packet %s'), var.get(u'line'))
                        return var.get('undefined')
                    finally:
                        if PyJsHolder_657272_68901310 is not None:
                            var.own[u'err'] = PyJsHolder_657272_68901310
                        else:
                            del var.own[u'err']
                        del PyJsHolder_657272_68901310
                var.get(u'self').callprop(u'_handlePacket', var.get(u'packet'))
            finally:
                    (var.put(u'i',Js(var.get(u'i').to_number())+Js(1))-Js(1))
        var.put(u'stream', var.get(u'packets').get((var.get(u'packets').get(u'length')-Js(1.0))))
    PyJs_anonymous_53_._set_name(u'anonymous')
    var.get(u"this").get(u'connection').callprop(u'on', Js(u'message'), PyJs_anonymous_53_)
PyJs_anonymous_48_._set_name(u'anonymous')
var.get(u'Scratch').get(u'CloudSession').get(u'prototype').put(u'_connect', PyJs_anonymous_48_)
@Js
def PyJs_anonymous_54_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([])
    if var.get(u"this").get(u'connection'):
        var.get(u"this").get(u'connection').callprop(u'close')
PyJs_anonymous_54_._set_name(u'anonymous')
var.get(u'Scratch').get(u'CloudSession').get(u'prototype').put(u'end', PyJs_anonymous_54_)
@Js
def PyJs_anonymous_55_(name, this, arguments, var=var):
    var = Scope({u'this':this, u'name':name, u'arguments':arguments}, var)
    var.registers([u'name'])
    return var.get(u"this").get(u'_variables').get(var.get(u'name'))
PyJs_anonymous_55_._set_name(u'anonymous')
var.get(u'Scratch').get(u'CloudSession').get(u'prototype').put(u'get', PyJs_anonymous_55_)
@Js
def PyJs_anonymous_56_(name, value, this, arguments, var=var):
    var = Scope({u'this':this, u'name':name, u'value':value, u'arguments':arguments}, var)
    var.registers([u'name', u'value'])
    var.get(u"this").get(u'_variables').put(var.get(u'name'), var.get(u'value'))
    var.get(u"this").callprop(u'_sendSet', var.get(u'name'), var.get(u'value'))
PyJs_anonymous_56_._set_name(u'anonymous')
var.get(u'Scratch').get(u'CloudSession').get(u'prototype').put(u'set', PyJs_anonymous_56_)
@Js
def PyJs_anonymous_57_(packet, this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments, u'packet':packet}, var)
    var.registers([u'packet'])
    while 1:
        SWITCHED = False
        CONDITION = (var.get(u'packet').get(u'method'))
        if SWITCHED or PyJsStrictEq(CONDITION, Js(u'set')):
            SWITCHED = True
            PyJs_Object_58_ = Js({})
            if PyJs_Object_58_.get(u'hasOwnProperty').callprop(u'call', var.get(u"this").get(u'variables'), var.get(u'packet').get(u'name')).neg():
                var.get(u"this").callprop(u'_addVariable', var.get(u'packet').get(u'name'), var.get(u'packet').get(u'value'))
            var.get(u"this").get(u'_variables').put(var.get(u'packet').get(u'name'), var.get(u'packet').get(u'value'))
            var.get(u"this").callprop(u'emit', Js(u'set'), var.get(u'packet').get(u'name'), var.get(u'packet').get(u'value'))
            break
        if True:
            SWITCHED = True
            var.get(u'console').callprop(u'warn', Js(u'Unimplemented packet'), var.get(u'packet').get(u'method'))
        SWITCHED = True
        break
PyJs_anonymous_57_._set_name(u'anonymous')
var.get(u'Scratch').get(u'CloudSession').get(u'prototype').put(u'_handlePacket', PyJs_anonymous_57_)
@Js
def PyJs_anonymous_59_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([])
    PyJs_Object_60_ = Js({})
    var.get(u"this").callprop(u'_send', Js(u'handshake'), PyJs_Object_60_)
PyJs_anonymous_59_._set_name(u'anonymous')
var.get(u'Scratch').get(u'CloudSession').get(u'prototype').put(u'_sendHandshake', PyJs_anonymous_59_)
@Js
def PyJs_anonymous_61_(name, value, this, arguments, var=var):
    var = Scope({u'this':this, u'name':name, u'value':value, u'arguments':arguments}, var)
    var.registers([u'name', u'value'])
    PyJs_Object_62_ = Js({u'name':var.get(u'name'),u'value':var.get(u'value')})
    var.get(u"this").callprop(u'_send', Js(u'set'), PyJs_Object_62_)
PyJs_anonymous_61_._set_name(u'anonymous')
var.get(u'Scratch').get(u'CloudSession').get(u'prototype').put(u'_sendSet', PyJs_anonymous_61_)
@Js
def PyJs_anonymous_63_(method, options, this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments, u'method':method, u'options':options}, var)
    var.registers([u'object', u'options', u'name', u'method'])
    PyJs_Object_64_ = Js({u'user':var.get(u"this").get(u'user').get(u'username'),u'project_id':var.get(u"this").get(u'projectId'),u'method':var.get(u'method')})
    var.put(u'object', PyJs_Object_64_)
    for PyJsTemp in var.get(u'options'):
        var.put(u'name', PyJsTemp)
        var.get(u'object').put(var.get(u'name'), var.get(u'options').get(var.get(u'name')))
    var.get(u"this").callprop(u'_sendPacket', (var.get(u'JSON').callprop(u'stringify', var.get(u'object'))+Js(u'\n')))
PyJs_anonymous_63_._set_name(u'anonymous')
var.get(u'Scratch').get(u'CloudSession').get(u'prototype').put(u'_send', PyJs_anonymous_63_)
@Js
def PyJs_anonymous_65_(data, this, arguments, var=var):
    var = Scope({u'this':this, u'data':data, u'arguments':arguments}, var)
    var.registers([u'data'])
    if PyJsStrictEq(var.get(u"this").get(u'connection').get(u'readyState'),var.get(u'WebSocket').get(u'OPEN')):
        var.get(u"this").get(u'connection').callprop(u'send', var.get(u'data'))
    else:
        var.get(u"this").get(u'attemptedPackets').callprop(u'push', var.get(u'data'))
PyJs_anonymous_65_._set_name(u'anonymous')
var.get(u'Scratch').get(u'CloudSession').get(u'prototype').put(u'_sendPacket', PyJs_anonymous_65_)
@Js
def PyJs_anonymous_66_(name, value, this, arguments, var=var):
    var = Scope({u'this':this, u'name':name, u'value':value, u'arguments':arguments}, var)
    var.registers([u'self', u'name', u'value'])
    var.put(u'self', var.get(u"this"))
    var.get(u"this").get(u'_variables').put(var.get(u'name'), var.get(u'value'))
    @Js
    def PyJs_anonymous_68_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([])
        return var.get(u'self').callprop(u'get', var.get(u'name'))
    PyJs_anonymous_68_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_69_(value, this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments, u'value':value}, var)
        var.registers([u'value'])
        var.get(u'self').callprop(u'set', var.get(u'name'), var.get(u'value'))
    PyJs_anonymous_69_._set_name(u'anonymous')
    PyJs_Object_67_ = Js({u'enumerable':var.get(u'true'),u'get':PyJs_anonymous_68_,u'set':PyJs_anonymous_69_})
    var.get(u'Object').callprop(u'defineProperty', var.get(u"this").get(u'variables'), var.get(u'name'), PyJs_Object_67_)
PyJs_anonymous_66_._set_name(u'anonymous')
var.get(u'Scratch').get(u'CloudSession').get(u'prototype').put(u'_addVariable', PyJs_anonymous_66_)
var.get(u'module').put(u'exports', var.get(u'Scratch'))
pass
