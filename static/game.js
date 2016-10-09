function removeBoard(tid){
  var body = document.getElementsByTagName("BODY")[0];
  var tbls= document.getElementsByClassName("board");

  for(var i=0;i<tbls.length;i++){
    if(tbls[i].dataset["id"]==tid){
      var e = tbls[i].parentNode;
      body.removeChild(e);
    }
  }
}

function addBoard(tid,name){
  var body = document.getElementsByTagName("BODY")[0];

  var div = document.createElement("DIV");
  div.className="parent";

  var tbl = document.createElement("TABLE");
  tbl.dataset["id"]=tid;
  tbl.className="board";
  for(var i=0;i<4;i++){
    var row = tbl.insertRow();
    for(var j=0;j<4;j++){
      row.insertCell();
    }
  }
  var p=document.createElement("P");
  p.dataset["id"]=tid;
  p.innerHTML="Score: 0";
  p.className="points";

  var pName=document.createElement("P");
  pName.dataset["id"]=tid;
  pName.innerHTML=name;
  pName.className="name";

  div.appendChild(pName);
  div.appendChild(p);
  div.appendChild(tbl);
  body.appendChild(div);
}

var gameBoard;

var colors=["#ccc0b2","#e5dbd1","#ece0c8","#f2b179","#f59563","#f59563","#f57c5f",
            "#f65d3b","#f65d3b","#edcc61","#ecc850","#edc53f","#edc53f"];

var socket = io.connect('http://' + document.domain + ':' + location.port);

function updateTables(board){
  board=board.split(" ");
  gameBoard=document.getElementsByClassName("board");
  boardNumber=parseInt(board[0]);
  var head=document.getElementsByClassName("points");
  for(var i=0;i<head.length;i++){
      if(head[i].dataset["id"]==boardNumber){
        head=head[i];
      }
  }
  head.innerHTML="Score: "+parseInt(board[1]);
  for(var i=0;i<gameBoard.length;i++){
    if(gameBoard[i].dataset["id"]==boardNumber){
      gameBoard=gameBoard[i];
      break;
    }
  }
  if(!gameBoard) return;
  for(var i=0;i<4;i++){
    for(var j=0;j<4;j++){
      var val=board[2+4*i+j];
      if(val!=0){
        gameBoard.rows[i].cells[j].innerHTML=Math.pow(2,val);
      }else {
        gameBoard.rows[i].cells[j].innerHTML=" ";
      }
      gameBoard.rows[i].cells[j].style.backgroundColor=colors[val];
    }
  }
}

socket.on("bupdate",function(board){updateTables(board)});

socket.on("load_others",function(games){
  for(var i=0;i<games.length;i++){
    addBoard(parseInt(games[i][0]),"other");
    updateTables(games[i]);
  }

});

socket.on("player_connect",function(uid,name){
  console.log(name,"connected with id",uid);
  addBoard(uid,name);
});

socket.on("player_disconnect",function(uid){
  console.log("player disconnected with id",uid);
  removeBoard(uid);
});

window.addEventListener("keydown",function(event){
  var key=event.keyCode;
  //if(key>=37 && key<=40)
    socket.emit("input",{key:event.keyCode});
});

document.addEventListener("load",function(){
  addBoard(1);
});
