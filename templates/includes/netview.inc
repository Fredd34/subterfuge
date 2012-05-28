{% load modextras %}


<!--

<div id = "nettitle">HTTP CodeInjection:&nbsp;&nbsp;</div>
<div id = "nettitle"><img width = "25" src = "/static/images/netview/red.png"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div>
<div id = "nettitle">Tunnel Block:&nbsp;&nbsp;</div>
<div id = "nettitle"><img width = "25" src = "/static/images/netview/green.png"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div>
<div id = "nettitle">EvilGrade:&nbsp;&nbsp;</div>
<div id = "nettitle"><img width = "25" src = "/static/images/netview/red.png"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div>

-->


<script type = "text/javascript">
function loading()
{
  $(".window").show("slow")
  $(".window").delay(3000).hide("slow");
}
</script>

{% if client %}
    {% for host in client %}
    
   <div id = "netclient" class = "netos{{ forloop.counter }}">
      <div id = "netos">
         <img width = "100" src = "/static/images/netview/{{ host.os }}.png">
      </div>
      <div id = "netoptions">
         <table>
            <tr>
               <td>
                  IP:
               </td>
               <td>
                  {{ host.address }}
               </td>
            </tr>
            <tr>
               <td>
                  MAC:
               </td>
               <td>
                  {{ host.mac }}
               </td>
            </tr>
            <tr>
               <td>
                  OS:
               </td>
               <td>
                  
               </td>
            </tr>
         </table>         
      </div>
         <a href = "#expand"  name = "expand{{ forloop.counter }}" class = "expand{{ forloop.counter }}"><div id = "redbutton2" style = "color: white;">Expand</div></a> 
         <a href = "javascript: loading()" name = "scan{{ host.address }}" class = "scan{{ host.address }}"><div id = "redbutton2" style = "color: white;">Scan</div></a>      
   </div>
   
   
   
   <div id = "expand{{ forloop.counter }}">
      <div id = "cont">
         <div id = "expand">
         
   <div id = "netos">
      <img width = "100" src = "/static/images/netview/{{ host.os }}.png">
   </div>
   <div id = "netoptions">
      <table>
         <tr>
            <td>
               IP:
            </td>
            <td>
               {{ host.address }}
            </td>
         </tr>
         <tr>
            <td>
               MAC:
            </td>
            <td>
               {{ host.mac }}
            </td>
         </tr>
         <tr>
            <td>
               OS:
            </td>
            <td>
               
            </td>
         </tr>
      </table>         
   </div>
      <a href = "#"  name = "shrink{{ forloop.counter }}" class = "shrink{{ forloop.counter }}"><div id = "redbutton2" style = "color: white;">Shrink</div></a>
      
      
      <script type="text/javascript">
			$(document).ready(function() {  
					 
					  //selects the scan link
				 $('a[name="scan{{ host.address }}"]').click(function(e) {
							//Cancel the link behavior
					  e.preventDefault();
							//Get the A tag
					  var id = $(this).attr('href');

							//Start Scan
					  $.post("/netctrl/scan/", { target: "{{ host.address }}" } );
					  
				 });         
			});  
      </script>
      <a href = "javascript: loading()" name = "scan{{ host.address }}" class = "scan{{ host.address }}"><div id = "redbutton2" style = "color: white;">Scan</div></a>    
      
   <div id = "expandbox">
      <div id = "netoptions">
         Open Ports:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      </div>
      
    {% for result in scan %}
      {% if result.address == host.address %}
         {% for port in result.ports|joinby %}
            <div id = "netoptions">
             {{ port }}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            </div>
         {% endfor %}
      {% endif %}
    {% endfor %}
   </div>
   
   
   <div id = "expandbox">
      <div id = "netoptions" class="modpanel{{ forloop.counter }}">
         Controls:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      </div>
      
    {% for module in modules %}
      <script type="text/javascript">
      $(document).ready(function() {  
         
                 //On Click
          $('a[name="ctrlpanel{{ forloop.counter }}c{{ forloop.parentloop.counter }}"]').click(function(e) {
                  //Cancel the link behavior
              e.preventDefault();
                  //Get the A tag
              var id = $(this).attr('href');
         
                  //Expanded View
               {% for host in client %}
                  {% for module in modules %}
                     $(".ctrlpanel{{ forloop.counter }}c{{ forloop.parentloop.counter }}").hide("slow");
                  {% endfor %}
               {% endfor %}
               $(".ctrlpanel{{ forloop.counter }}c{{ forloop.parentloop.counter }}").delay(1000).show("slow");
      
          });
      });  
      </script>
      
      <div id = "netoptions" class="modpanel{{ forloop.counter }}">
       <a href="#" name="ctrlpanel{{ forloop.counter }}c{{ forloop.parentloop.counter }}"><img height="65" width="65" src="/static/images/plugins/{{ module.name }}.png"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      </div>
      

     
      
    {% endfor %}
   </div>


    
         </div>
      </div>
   </div>
   
   
<script type="text/javascript">
$(document).ready(function() {
{% if host.expand == "0" %}
   $("#expand{{ forloop.counter }}").hide();
{% else %}
   $(".netos{{ forloop.counter }}").hide();
{% endif %}
});
$(document).ready(function() {  
       
        //selects the link
    $('a[name="expand{{ forloop.counter }}"]').click(function(e) {
            //Cancel the link behavior
        e.preventDefault();
            //Get the A tag
        var id = $(this).attr('href');
   
            //Expanded View
        $("#expand{{ forloop.counter }}").delay(1000).show("slow");
        $(".netos{{ forloop.counter }}").hide("slow");

    });         
});
$(document).ready(function() {  
       
        //selects the link
    $('a[name="shrink{{ forloop.counter }}"]').click(function(e) {
            //Cancel the link behavior
        e.preventDefault();
            //Get the A tag
        var id = $(this).attr('href');
   
            //Expanded View
        $("#expand{{ forloop.counter }}").hide("slow");
        $(".netos{{ forloop.counter }}").delay(1000).show("slow");

    });         
});  
</script>


    {% endfor %}
{% endif %}







<!-- Recheck Arp Poison -->

<script type="text/javascript">
{% if status == "on" %}
	$(document).ready(function () {
	  $("#startpwn").hide("slow")
	});
	$(document).ready(function () {
	  $("#onbar").show("slow");
	});
	$(document).ready(function () {
	  $("#stoppwn").show("slow");
	});
{% else %}
	$(document).ready(function () {
	  $("#startpwn").show("slow");
	});
	$(document).ready(function () {
	  $("#onbar").hide("slow")
	});
	$(document).ready(function () {
	  $("#stoppwn").hide("slow");
	});

{% endif %}
</script>