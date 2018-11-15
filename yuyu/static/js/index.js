
var input
var span
var timer

window.onload=function(){

    input = $('input.start')
    span = $('span.start')
    var timer_id = span.attr('timer_id')
    // var starttime = span.attr('starttime')
    if (timer_id && ! timer){
        input.val('结束')
        timer = setInterval(starttime,500)
    }
    


}


function starttime() {
    var now = new Date().getTime() - span.attr('starttime')
    now = now / 1000

    // if (now>1200){
    //     audioAutoPlay()
    //     window.clearInterval(timer);
    // }

    hour = Math.floor(now/3600)
    minute = Math.round(now%3600)
    second = Math.round(minute%60)
    minute = Math.floor(minute/60)
    span.text(bw(hour) + ":" + bw(minute) + ":" + bw(second))

}

function start() {
    if (input.val() == '开始'){
        input.val('结束')
        var timestamp = new Date().getTime()
        span.attr('starttime',timestamp)
        timer=setInterval(starttime,500)

        myajax({'id':-1})
        window.location.href = "https://itunes.apple.com/cn/app/id1049758801";
    }
    else{
        input.val('开始')
        window.clearInterval(timer);
        span.text('00:00:00')
        var audio = document.getElementById("bgMusic")
        audio.pause()

        myajax({'id':span.attr('timer_id')})
    }
}

function bw(num) {
    return PrefixInteger(num, 2)
}

function PrefixInteger(num, n) {
    return (Array(n).join(0) + num).slice(-n);
}

function audioAutoPlay() {
    var audio = document.getElementById("bgMusic"),
    play = function () {
        audio.play();
        document.removeEventListener("touchstart", play, false);
    };
    audio.play();
    document.addEventListener("WeixinJSBridgeReady", function () {
        play();
    }, false);
    document.addEventListener('YixinJSBridgeReady', function () {
        play();
    }, false);
    document.addEventListener("touchstart", play, false);
}


function myajax(dict) {
    $.ajax({
        url:'/opt_timer/',
        data:dict,
        type:"get",
        datatype:"json",
        success:function(data){
            if (data == 'redirect'){
                location.reload()
            }
            span.attr('timer_id',data)
        },
        error:function(err){
            alert('err:'+err)
            // document.write('run_ajax 出错了')
        }
    })
}






// var hour,minute,second;//时 分 秒
//     hour=minute=second=0;//初始化
//     var millisecond=0;//毫秒
//     var int;
//     function Reset()//重置
//     {
//       window.clearInterval(int);
//       millisecond=hour=minute=second=0;
//       document.getElementById('timetext').value='00时00分00秒000毫秒';
//     }
  
//     function start()//开始
//     {
//       int=setInterval(timer,50);
//     }
  
//     function timer()//计时
//     {
//       millisecond=millisecond+50;
//       if(millisecond>=1000)
//       {
//         millisecond=0;
//         second=second+1;
//       }
//       if(second>=60)
//       {
//         second=0;
//         minute=minute+1;
//       }
  
//       if(minute>=60)
//       {
//         minute=0;
//         hour=hour+1;
//       }
//       document.getElementById('timetext').value=hour+'时'+minute+'分'+second+'秒'+millisecond+'毫秒';
  
//     }
  
//     function stop()//暂停
//     {
//       window.clearInterval(int);
//     }