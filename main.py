from urllib import request, parse
#from crypto import #something

SERVER = 'scratch.mit.edu'
PROJECTS_SERVER = 'projects.scratch.mit.edu'
CDN_SERVER = 'cdn.scratch.mit.edu'
CLOUD_SERVER = 'clouddata.scratch.mit.edu'
API_SERVER = 'api.scratch.mit.edu'

def request(options):
    headers={
        'Cookie': 'scratchcsrftoken=a; scratchlanguage=en;',
        'X-CSRFToken': 'a',
        'referer': 'https://scratch.mit.edu' #Required by Scratch servers
    }
    if options.headers!=[]:
        for index,name in enumerate(options.headers):
            headers[index]=options.headers[index]

    if options.body!=[]:
        headers[headers.index('Content-Length')] = Buffer.byteLength(options.body) #What is this?
    if options.sessionId!=[]:
        headers.Cookie += 'scratchsessionsid=' + options.sessionId + ';'
        
        
    params = {
        hostname: options.hostname || SERVER,
        port: 443,
        path: options.path,
        method: options.method || 'GET',
        headers: headers
        }
    
    querystring=parse.urlencode(params)
    u=request.urlopen(url+'?'+querystring)
    resp=u.read()
    
    parts = []
    
    #IDK what this does
    #response.on('data', function(chunk) { parts.push(chunk); });
    #response.on('end', function() { cb(null, Buffer.concat(parts).toString(), response); });
    
    #req.on('error', cb);
    #  if (options.body) req.write(options.body);
    #  req.end();
    
def requestJSON(options):
    request(options)
    try:
        JSON.parse(body)
    catch exc:
        print(exc)
        
def parseCookie(cookie):
    cookies = {};
    each = cookie.split(';');
    i = each.length;
    rep=true
    while rep:
        if (each[i].indexOf('=') == -1):
            rep=false
        var pair = each[i].split('=');
        cookies[pair[0].trim()] = pair[1].trim();
    return cookies

class Scratch:
    def getProject(projectId):
        requestJSON({
            hostname: PROJECTS_SERVER,
            path: '/' + projectId,
            method: 'GET'
        })
        
  # def getProjects = username, cb) {
  #requestJSON({
  #  hostname: API_SERVER,
  #  path: '/users/' + username + '/projects',
  #  method: 'GET'
  #}, cb);
