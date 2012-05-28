<div id="credbg">
<table class="credlist">
<tr class = "credbar">
<td>Source</td>
<td>Username</td>
<td>Password</td>
<td>Date</td>
</tr>

{% if credential %}
    {% for cred in credential %}
        <tr class = "{% cycle 'credrowa' 'credrowb' %}">
            <td width = "271">{{ cred.source }}</td>
            <td width = "374">{{ cred.username }}</td>
            <td width = "361">{{ cred.password }}</td>
            <td width = "120">{{ cred.date }}</td>
        </tr>
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

</table>
</div>
