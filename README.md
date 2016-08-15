## this is wha I am tring to do here 
http://stackoverflow.com/questions/38887079/find-a-pattern-in-html-and-replace-it-with-php-code/38887778#38887778


my actual files might look like this so reflected this in the new file in the html_files directory
	<!-- Footer part at bottom of page-->
	<div id="footer">
       <div class="row col-md-2 col-md-offset-5">
			
		<p class="text-muted">&copy; 2014. Core Team</p>
      </div>

		<div id="downloadlinks">
		<!-- this is what i am trying to automate/multle times-->
		<!--<a href="UMTS_Cell_Day(partB).csv"
		class="glyphicon glyphicon-download-alt text-muted">
		</a>
		<a href="UMTS_Cell_Day(partB).csv"
		class="glyphicon glyphicon-download-alt text-muted">
		</a>
		<a href="UMTS_Cell_Day(partB).csv"
		class="glyphicon glyphicon-download-alt text-muted">
		</a> --> 
		</div>
    </div>

	
	## awk taht he will delete , but it does not work and is on a different version of awk
	awk 'FNR==1{ARGIND++} ARGIND==1{old=$0;next} ARGIND==2{new=$0;next}
    {rec = rec $0 RS }
    END{ if (s=index(rec,old)) { rec = substr(rec,1,s-1) new substr(rec,s+length(old)) } printf "%s", rec }' old new file


	## Q2 
	http://stackoverflow.com/questions/38909629/counting-the-number-of-time-a-pattern-occurs-in-files/38922053#38922053
	
	