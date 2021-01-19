heading = 'Grey Notification'
subHeading = 'Render Error'
content = 'The order of the render items is to be reduced in the particular'


msgContent = f"""\
<!DOCTYPE html>
<html>
    <body style="margin: 0px;
	padding: 0px;
	background: #22222D url(images/img01.png) repeat;
	font-family: 'Open Sans', sans-serif;
	font-size: 13px;
	color: #545454;">
        <div id ="wrapper" style="overflow: hidden;
        width: 1200px;
        margin: 50px auto;
        background: #FFFFFF;
        box-shadow: 0px 0px 150px 5px rgba(0,0,0,.2);">
        <div id="wrapper" style="overflow: hidden;
                                width: 100%;
                                margin: 0px auto;
                                background: #FFFFFF;
                                box-shadow: 0px 0px 10px 5px rgba(0,0,0,.2);">

            <div id="header" style="overflow: hidden;
                                    height: 150px;
                                    background: #000000;
                                    font-family:monospace;">
                                
                        <div id="border" style="margin:50px;">
                                <h1 style="text-decoration: none;
                                font-size: 26px;
                                font-weight: 100;
                                font-family:monospace;
                                color: #FFFFFF;
                                
                                ">
                                           {heading} </h1>
                                           {subHeading}
                        </div>
                    
            </div>

            <div id="page" style="overflow: hidden;
            width: 100%;
            padding: 50px 50px 50px 50px;
            background: #F6F6F6 url(images/img01.png) repeat;
            color: #202020;">
            
            <p style="width:84%">
            {content}
</p>
            </div>                         
    </div>
        </div>
    </body>
</html>
"""

print(msgContent)

