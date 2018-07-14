$(document).ready(function () {
    $("#smsBtn").bind("click", function () {
        data = {"phoneNum":$("#phone").val()};
        console.log(data);
        $.ajax({
            url:"/login/",
            data:data,
            dataType:"json",
            type:"get",
            success:function(data, status){
                console.log(data);
            }
        });
    });
});