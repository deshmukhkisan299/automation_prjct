function calc(){
   let x = document.getElementById("qunt_id").value;
   let y = document.getElementById("cost_id").innerHTML;
   document.getElementById("total_id").innerHTML = x*y;
   
   
   var table= document.getElementById("table");
   sumVal= 0;
   
   for(var i = 1; i<table.rows.length; i++){
      sumVal = sumVal + parseInt(table.rows[i].cells[3].innerHTML);
      document.getElementById("final_total").innerHTML = sumVal;
   }
   
  
  
}