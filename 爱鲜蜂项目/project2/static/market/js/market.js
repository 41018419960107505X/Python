$(document).ready(function () {
    // http://127.0.0.1:8000/market/103606/
    var url = location.href;
    spanIdStr = "yellow" + url.split("/")[4]
    $yellowSpan = $(document.getElementById(spanIdStr))
    $yellowSpan.addClass("yellowSlide")


    //点击分类和排序
    $("#allTypeBtn").bind("click", function () {
        $("#typediv").toggle();
        $("#sortdiv").hide();
    });
    $("#allSortBtn").bind("click", function () {
        $("#sortdiv").toggle();
        $("#typediv").hide();
    });
    $("#typediv").bind("click", func);
    $("#sortdiv").bind("click", func);
    function func() {
        $(this).hide()
    }


    //给分类添加颜色
    aIdStr = "type" + url.split("/")[5]
    $a = $(document.getElementById(aIdStr))
    $a.addClass("abg")


    function changeCart(){
        var flag = $(this).attr("flag");
        //组id  子组id  商品id
        var gid = $(this).attr("gid");
        var cid = $(this).attr("cid");
        var pid = $(this).attr("pid");
        console.log(gid,cid,pid);
        //发起ajax请求，添加购物车
        $.post("/changecart/"+flag+"/", {"gid":gid,"cid":cid,"pid":pid}, function (data, status) {
            if (data.error){
                location.href = "http://127.0.0.1:8000/login/"
            } else {
                $(document.getElementById(pid)).html(data.num)
            }
        });
    }


    //添加购物车
    $(".addBtn").bind("click", changeCart);
    $(".subBtn").bind("click", changeCart);
});