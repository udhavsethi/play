var http = require('http');
var os = require('os');

const hostname = '0.0.0.0';
const port = 4040;

http.createServer(function (req, res) {
  console.log(`ping received on ${os.hostname()}`)
  res.write('pong');
  res.end();
}).listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
