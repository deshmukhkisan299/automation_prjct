$(document).ready(function()
   {
      $("tr").each(function()
      {
         var totalmarks = 0;
         $(this).find('.').each(function()
         {
            var marks=$(this).text();
            if(marks.length !==0)
            {
               totalmarks+=parseFloat(marks);
            }
         });
         $(this).find('.').html(totalmarks)
      });
      
   });