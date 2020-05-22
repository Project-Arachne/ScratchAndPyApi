from urllib import request, parse
#from crypto import #something (If needed)

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
        
    if options.hostname=""
        host=SERVER
    else:
        host=options.hostname
    
    if method=""
        method='GET'
    else:
        method=options.method
    params = {
        hostname: host,
        port: 443,
        path: options.path,
        method: method,
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
    except exc:
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
        
    def UserSession(username, id, sessionId):
        self.username = username;
        self.id = id;
        self.sessionId = sessionId;
    
    def UserSession.create(username, password):
        try:
            request({
                path: '/login/',
                method: 'POST',
                body: JSON.stringify({username: username, password: password}),
                headers: {'X-Requested-With': 'XMLHttpRequest'}
            }
            user = JSON.parse(body)[0];
            return new Scratch.UserSession(user.username, user.id, parseCookie(response.headers['set-cookie'][0]).scratchsessionsid));
        except err:
            print("error:",err)
    
    def UserSession.prompt():
        uname=input("Enter username")
        pass=input("Enter password")
        Scratch.UserSession.create(uname, pass)
    
    def UserSession.load():
        prompt()
        session._saveSession()
        
    def readFile(SESSION_FILE):
    #WIP, need to implement file saving
    
    #var obj = JSON.parse(data.toString());
    #var session = new Scratch.UserSession(obj.username, obj.id, obj.sessionId);
    #session.verify(function(err, valid) {
    #  if (err) return cb(err);
    #  if (valid) return cb(null, session);
    #  prompt();
    
    def UserSession.saveSession():
        writeFile(SESSION_FILE, JSON.stringify({
        username: self.username,
    	id: self.id,
        sessionId: self.sessionId
        }))
    
    def UserSession.verify():
        request({
            path: '/messages/ajax/get-message-count/', # probably going to change quite soon
            sessionId: self.sessionId
        })
        if response.statusCode == 200:
            return true
        else:
            return false
    
    def UserSession.getAllProjects():
        requestJSON({
            hostname: SERVER,
            path: '/site-api/projects/all/',
            method: 'GET',
            sessionId: self.sessionId
        })
        
    def UserSession.setProject(projectId, payload):
        if payload.type() !== str:
            payload = JSON.stringify(payload)
            requestJSON({
                hostname: PROJECTS_SERVER,
                path: '/internalapi/project/' + projectId + '/set/',
                method: 'POST',
                body: payload,
                sessionId: self.sessionId

    def UserSession.getBackpack():
        requestJSON({
            hostname: SERVER,
            path: '/internalapi/backpack/' + self.username + '/get/',
            method: 'GET',
            sessionId: self.sessionId
        })

    def UserSession.setBackpack = function(payload, cb) {
        if (payload.type() !== str):
          payload = JSON.stringify(payload);
        requestJSON({
          hostname: SERVER,
          path: '/internalapi/backpack/' + self.username + '/set/',
          method: 'POST',
          body: payload,
          sessionId: self.sessionId
        })
        
    def UserSession.addComment(options):
        if options.project!='' {
            type = 'project';
            id = options.project;
        } elif options.user!='' {
            type = 'user';
            id = options.user;
        } elif options.studio!='' {
            type = 'gallery';
            id = options.studio;
        }
        request({
            hostname: SERVER,
            path: '/site-api/comments/' + type + '/' + id + '/add/',
            method: 'POST',
            body: JSON.stringify({
                content: options.content,
                parent_id: options.parent || '',
                commentee_id: options.replyto || '',
            }),
        sessionId: self.sessionId
        })
        
    def UserSession.cloudSession(projectId):
        Scratch.CloudSession._create(self, projectId)
        
        
        #DONE UP TO HERE

    def CloudSession():
        self.user = user
        self.projectId = '' + projectId
        self.connection = null
        self.attemptedPackets = [];
        self.variables = Object.create(null)
        self._variables = Object.create(null)

    #util.inherits(Scratch.CloudSession, events.EventEmitter);
    #What does this do?
        
    def CloudSession._create(user, projectId):
        session = Scratch.CloudSession(user, projectId)
        session._connect()
        
    def CloudSession._connect():
        self.connection = new WebSocket('wss://' + CLOUD_SERVER + '/', [], {
            headers: {
                cookie: 'scratchsessionsid=' + self.user.sessionId + ';',
                origin: 'https://scratch.mit.edu'
            }
        })

#Replace these with correct callbacks
  #self.connection.on('open', function() {
  #  self._sendHandshake();
  #  for (var i = 0; i < self.attemptedPackets.length; i++) {
  #    self._sendPacket(self.attemptedPackets[i]);
  #  }
  #  self.attemptedPackets = [];
  #  if (cb) cb();
  #});

  #self.connection.on('close', function() {
  #  #Reconnect because Scratch disconnects clients after no activity
  #  #Probably will cause some data to not be pushed
  #  self._connect();
  #});

  #var stream = '';
  #self.connection.on('message', function(chunk) {
  #  stream += chunk;
  #  var packets = stream.split('\n');
  #  for(var i = 0; i < packets.length - 1; i++) {
  #    var line = packets[i];
  #    var packet;
  #    try {
  #      packet = JSON.parse(line);
  #    } catch (err) {
  #      console.warn('Invalid packet %s', line);
  #      return;
  #    }
  #    self._handlePacket(packet);
  #  }
  #  stream = packets[packets.length - 1];
  #});
#};
    def CloudSession.end():
        if self.connection!="":
            self.connection.close()

    def CloudSession.get(name):
        return self._variables[name]
        
    def CloudSession.set(name, value):
        self._variables[name] = value
        self._sendSet(name, value)
        
    def CloudSession._handlePacket(packet):
        pass
       #IDK what to do with this
    #  switch (packet.method) {
    #    case 'set':
    #      if (!({}).hasOwnProperty.call(self.variables, packet.name)) {
    #        self._addVariable(packet.name, packet.value);
    #      }
    #      self._variables[packet.name] = packet.value;
    #      self.emit('set', packet.name, packet.value);
    #      break;
    #    default:
    #      console.warn('Unimplemented packet', packet.method);
    #  }
    #};

    def CloudSession._sendHandshake():
      self._send('handshake', {})
      
    def CloudSession._sendSet(name, value):
        self._send('set', {
            name: name,
            value: value
        })
        
    def CloudSession._send(method, options):
        object = {
            user: self.user.username,
            project_id: self.projectId,
            method: method
      }
      for (name in options):
          object[name] = options[name]
      
      self._sendPacket(JSON.stringify(object) + '\n')
        
    def CloudSession._sendPacket(data):
        if (self.connection.readyState == WebSocket.OPEN):
            self.connection.send(data)
        else:
            self.attemptedPackets.push(data)
        
    def CloudSession._addVariable(name, value):
        self = self;
        self._variables[name] = value;
        #What is this?
        Object.defineProperty(self.variables, name, {
            enumerable: true,
            get: function() {
                return self.get(name);
            },
            set: function(value) {
                self.set(name, value);
            }
        })

module.exports = Scratch;
