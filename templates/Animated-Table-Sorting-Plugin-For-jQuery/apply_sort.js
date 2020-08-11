$(document).ready(function() {
    var i;
    for (i = 0; i < 15; i++) {
        var x = Math.floor((Math.random() * 3));
        var distance = (Math.random() * 10).toFixed(1);
        var time = Math.round(Math.sqrt(distance)*2)
        if(x==0){
            var dick = "<tr class='block safe'><td class='text safe'>0</td><td><h4>"+time+"分鐘</h4></td><td>"+distance+"公里</td></tr>";
        } else if(x==1){
            var dick = "<tr class='block warning'><td class='text warning'>1</td><td><h4>"+time+"分鐘</h4></td><td>"+distance+"公里</td></tr>";
        } else if(x==2){
            var dick = "<tr class='block danger'><td class='text danger'>2</td><td><h4>"+time+"分鐘</h4></td><td>"+distance+"公里</td></tr>";
        }
        $("table").append(dick);
    }
    $("table").tableSort( {
    animation :'slide',
    speed:600
    } );
    
    
    var looptime =0;
    function sort_by_category(){
        setTimeout(function(){
            $("table tr th.col-0").trigger('click');
            looptime++;
            if (looptime<5){
                sort_by_category();
            }
        },5000);
    }
    function sort_by_time(){
        setTimeout(function(){
            $("table tr th.col-1").trigger('click');
            looptime++;
            if (looptime<2){
                sort_by_time();
            }
        },5000);
    }
    function sort_by_distance(){
        setTimeout(function(){
            $("table tr th.col-2").trigger('click');
            looptime++;
            if (looptime<2){
                sort_by_distance();
            }
        },5000);
    }
    sort_by_category();
    
})
    