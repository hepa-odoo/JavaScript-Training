async function gettingOdooData()
  {
    let getOdooData = new Promise(function (resolve,reject) 
    {
      let req = new XMLHttpRequest();
      req.responseType = 'json';
      req.open('GET', 'odooGetData');
      req.onload = function() {
        if (req.status == 200) {
          setTimeout(()=>resolve(this.response),1000);
        } else {
          reject("Error: " + req.status);
        }
      }
      req.send();
    });
    document.getElementById('text-result').innerHTML="loading... gathering data<br>";
    
    let json_data = await getOdooData.catch((error)=>{
      return "error";
    });
    if(json_data=="error"){
      alert("Caught an error in gathering data!!!!");
      document.getElementById('text-result').innerHTML= "Caught an error in gathering data!!!!<br/><br/>";
    }
    else{
      document.getElementById('text-result').innerHTML= getCards(json_data);
    }
}

const getCards = (json_data) => {
  let id="";
  let name="";
  let card_html="<div id='property_cards' style='width:100%,height:100%,display:flex,flex-wrap:wrap'>";
  for(let x in json_data){
    id = json_data[x]["id"];
    name = json_data[x]["name"]
    card_html+=
    "<div class='card' style='width:150px,height:200px,background-color:white'>"+
    "<center><span>id : "+id+"</span></center>"+
    "<center><span>name : "+name+"</span></center>"+
    "<div>";
  }
  card_html+="</div>";
  return card_html;
}
