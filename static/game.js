function getUID() {
   var metas = document.getElementsByTagName('meta');

   for (var i=0; i<metas.length; i++) {
      if (metas[i].getAttribute("property") == "uid") {
         return metas[i].getAttribute("content");
      }
   }
    return "";
}

function addBoard(tid){

  var x = document.createElement("TABLE");
  console.log(x);
  window.appendChild(x);
}

var gameBoard;

var colors=["#fff","#aaf","#55f","#00f","#3ff","#0ff"];

var socket = io.connect('http://' + document.domain + ':' + location.port);

socket.on("bupdate",function(board){
  console.log(board);
  gameBoard=document.getElementById("board");
  for(var i=0;i<4;i++){
    for(var j=0;j<4;j++){
      var val=board[4*i+j];
      if(val!=0){
        gameBoard.rows[i].cells[j].innerHTML=Math.pow(2,val);
      }else {
        gameBoard.rows[i].cells[j].innerHTML=" ";
      }
      gameBoard.rows[i].cells[j].style.backgroundColor=colors[val];
    }
  }
});

window.addEventListener("keydown",function(event){
  socket.emit("input",event.keyCode);
});

document.addEventListener("load",function(){
  addBoard(1);
});
