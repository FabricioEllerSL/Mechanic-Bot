var app = require('express')();
var http = require('http');
var server = http.Server(app)
var io = require('socket.io')(server);
var port = process.env.PORT || 3000;
const botUrl = "http://127.0.0.1:5000/response/";

app.get('/', function (req, res) {
  res.sendFile(__dirname + '/public/index.html');
});

getBotResponse = (msg) => {
  let data = "";

  http.get(botUrl + msg, (response) => {
    response.on("data", (chunk) => {
      data += chunk;
    });

    response.on("end", () => {
      io.emit('chat message', "Mechanic Bot: " + data);
    });

  })  
}

io.on('connection', function (socket) {
  socket.on('chat message', function (msg) {
    io.emit('chat message', "you: " + msg);
    getBotResponse(msg);
  });
});

server.listen(port, function () {
  console.log('listening on *:' + port);
});
