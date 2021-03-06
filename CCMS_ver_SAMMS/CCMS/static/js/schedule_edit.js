/* CSRFToken*/
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

/* 日付フォーマット変換関数 */
function replaceDate(dateStr) {
  const regexp = /^([0-9]{2,4})-([0-1][0-9])-([0-3][0-9])(?:( [0-2][0-9]):([0-5][0-9]):([0-5][0-9]))?$/;
  return dateStr.replace(regexp, (match, year, month, day, hour, minutes, seconds) => {
    return `${year}-${month}-${day} ${hour}:${minutes}:${seconds}`;
  });
}

/* ページ初期処理. */
function initializePage() {
    // カレンダーの設定
    $('#calendar').fullCalendar({
        height: 550,
        lang: "ja",
        header: {
            left: 'prev,next today',
            center: 'title',
            right: 'month,basicWeek,basicDay'
        },
        timeFormat: 'HH:mm',
        selectable: true,
        selectHelper: true,
        navLinks: true,
        eventSources: [{
            url: "http://127.0.0.1:8000/getCalendar",
            dataType: 'json',
            async: false,
            type : 'GET',
            error: function() {
                $('#script-warning').show();
            }
        }],
        
        select: function(start, end, resource) {
            // 日付選択された際のイベント

            // ダイアログタイトル設定
            $("#dialogTitle").text("スケジュール登録");

            // ダイアログタイトル(メンテナンス予約)設定
            $("#menteDialogTitle").text("メンテナンス予定登録");
    
            // タイトル初期化
            $("#inputTitle").val("");
            // 備考初期化
            $("#inputDescription").val("");
            // ボタン制御
            $("#registButton").show();
            $("#updateButton").hide();
            $("#deleteButton").hide();
    
            // ダイアログ表示
            $('#inputScheduleForm').on('show.bs.modal', function (event) {
                setTimeout(function(){
                    $('#inputTitle').focus();
                }, 500);
            }).modal("show");

            // 日付ピッカーの設定
            $('#inputYmdFrom').datetimepicker({locale: 'ja', format : 'YYYY年MM月DD日', useCurrent: false });
            $('#inputYmdTo').datetimepicker({locale: 'ja', format : 'YYYY年MM月DD日', useCurrent: false });
            $('.ymdHm').datetimepicker({
                locale: 'ja',
                format : 'YYYY年MM月DD日 HH時mm分'
            });
    
            // 開始終了が逆転しないように制御
            $("#inputYmdHmFrom").on("dp.change", function (e) {
                $('#inputYmdHmTo').data("DateTimePicker").minDate(e.date);
            });
            $("#inputYmdHmTo").on("dp.change", function (e) {
                $('#inputYmdHmFrom').data("DateTimePicker").maxDate(e.date);
            });
    
            // 終日チェックボックス
            $('#allDayCheck').prop("checked", true);
            
            // 選択された日付をフォームにセット
            // FullCalendar の仕様で、終了が翌日の00:00になるため小細工
            var startYmd = moment(start);
            var endYmd = moment(end);
            if (endYmd.diff(startYmd, 'days') > 1) {
                endYmd = endYmd.add(-1, "days");
            } else {
                endYmd = startYmd;
            }
            $('#inputYmdFrom').val(startYmd.format("YYYY年MM月DD日"));
            $('#inputYmdFrom').data("DateTimePicker").date(startYmd.format("YYYY年MM月DD日"));
            $('#inputYmdTo').val(endYmd.format("YYYY年MM月DD日"));
            $('#inputYmdTo').data("DateTimePicker").date(endYmd.format("YYYY年MM月DD日"));

            startYmd = moment(formatNengappi($("#inputYmdFrom").val(), 0));
            endYmd = moment(formatNengappi($("#inputYmdTo").val(), 0));
            var startYmdHm = moment(startYmd.format("YYYY-MM-DD") + " " + "00:00");
            var endYmdHm = moment(startYmd.format("YYYY-MM-DD") + " " + "23:59");
            $("#inputYmdHmFrom").val(startYmdHm.format("YYYY年MM月DD日 HH時mm分"));
            $("#inputYmdHmTo").val(endYmdHm.format("YYYY年MM月DD日 HH時mm分"));
            $('.ymdHm').show();
            $('.ymd').hide();
        },
        eventClick: function(event) {
            // 予定クリック時のイベント
            console.log(event);
            $("#dialogTitle").text("スケジュール詳細");
    
            // ユーザーCD設定
            $("#userCd").val(event.user_cd);
            // スケジュールID設定
            $("#scheduleId").val(event.id);
            // タイトル設定
            $("#inputTitle").val(event.title);
            // 備考設定
            $("#inputDescription").val(event.description);

            // ボタン制御
            $("#registButton").hide();
            $("#updateButton").show();
            $("#deleteButton").show();
    
            // ダイアログ表示
            $('#inputScheduleForm').on('show.bs.modal', function (event) {
                setTimeout(function(){
                    $('#inputTitle').focus();
                }, 500);
            }).modal("show");
    
            // 日付ピッカーの設定
            $('.ymdHm').hide()
            $('#inputYmdFrom').datetimepicker({locale: 'ja', format : 'YYYY年MM月DD日', useCurrent: false });
            $('#inputYmdTo').datetimepicker({locale: 'ja', format : 'YYYY年MM月DD日', useCurrent: false });
            $('.ymdHm').datetimepicker({
                locale: 'ja',
                format : 'YYYY年MM月DD日 HH時mm分'
            });
    
            // 開始終了が逆転しないように制御
            $("#inputYmdFrom").on("dp.change", function (e) {
                $('#inputYmdTo').data("DateTimePicker").minDate(e.date);
            });
            $("#inputYmdTo").on("dp.change", function (e) {
                $('#inputYmdFrom').data("DateTimePicker").maxDate(e.date);
            });
    
            // 終日チェックボックス
            $('#allDayCheck').prop("checked", true);
    
            // 選択された日付をフォームにセット
            // FullCalendar の仕様で、終了が翌日の00:00になるため小細工
            var startYmd = moment(event.start);
            var endYmd = moment(event.end);
            if (endYmd.diff(startYmd, 'days') > 1) {
                endYmd = endYmd.add(-1, "days");
            } else {
                endYmd = startYmd;
            }
            $('#inputYmdFrom').val(startYmd.format("YYYY年MM月DD日"));
            $('#inputYmdFrom').data("DateTimePicker").date(startYmd.format("YYYY年MM月DD日"));
            $('#inputYmdTo').val(endYmd.format("YYYY年MM月DD日"));
            $('#inputYmdTo').data("DateTimePicker").date(endYmd.format("YYYY年MM月DD日"));
        },
        editable: true,
        eventLimit: true
    });
}

/* 予定入力フォームの登録ボタンクリックイベント. */
function registSchedule() {
    var elements = document.getElementById("menteCarSelect");
    var radioNodeList = elements.selectCar;
    var carName = radioNodeList.value;
    
    var startYmd = moment(formatNengappi($('#inputYmdFrom').val(), 1));
    var endYmd = moment(formatNengappi($('#inputYmdTo').val(), 1)).add(23, "hours").add(59, "minutes");
    var allDayCheck = $('#allDayCheck').prop("checked");
    if (!allDayCheck) { //allDayのチェックがないとき
        startYmd = moment(formatNengappi($('#inputYmdHmFrom').val(), 1));
        endYmd = moment(formatNengappi($('#inputYmdHmTo').val(), 1));
    }
    if (endYmd.diff(startYmd, 'days') > 0) {
        endYmd = endYmd.add(+1, "days");
    }
    var eventData;
    if (carName !== "") {
        eventData = {
            title: carName,
            start: startYmd.format("YYYY-MM-DD HH:mm:ss"),
            end: endYmd.format("YYYY-MM-DD HH:mm:ss"),
            allDay: allDayCheck,
            description: $('#inputDescription').val(),
        };
        $.ajax({
            url: "http://127.0.0.1:8000/registCalendar",
            type: "POST",
            cache:false,
            data: JSON.stringify(eventData),
            success: function() {
                $('#fullcalendar').fullCalendar( 'refetchEvents' );
                alert(carName + 'のメンテナンスを登録しました。');
                location.reload();     
            },
            error: function() {
            }
        });
    }
    $('#calendar').fullCalendar('unselect');
}
    
/* 予定入力フォームの更新ボタンクリックイベント. */
function updateSchedule() {
    
    var startYmd = moment(formatNengappi($('#inputYmdFrom').val() + "00時00分00", 1));
    var endYmd = moment(formatNengappi($('#inputYmdTo').val() + "00時00分00", 1));
    var allDayCheck = $('#allDayCheck').prop("checked");
    if (!allDayCheck) {
        startYmd = moment(formatNengappi($('#inputYmdFrom').val() + "00時00分00", 1));
        endYmd = moment(formatNengappi($('#inputYmdTo').val() + "00時00分00", 1));
    }
    if (endYmd.diff(startYmd, 'days') > 0) {
        endYmd = endYmd.add(+1, "days");
    }
    
    var eventData;
    if ($('#inputTitle').val()) {
        eventData = {
            user_cd: $("#userCd").val(),
            id: $("#scheduleId").val(),
            title: $('#inputTitle').val(),
            start: startYmd.format("YYYY-MM-DDTHH:mm:ss"),
            end: endYmd.format("YYYY-MM-DDTHH:mm:ss"),
            allDay: allDayCheck,
            description: $('#inputDescription').val()
        };
        filter = {
            user_cd: $("#userCd").val(),
            id: $("#scheduleId").val()
        }
        $.ajax({
            url: "http://localhost:8080/update",
            type: "POST",
            data: JSON.stringify(eventData),
            success: function(jsonResponse) {
                // 再描画
                $('#calendar').fullCalendar('removeEvents');
                $('#calendar').fullCalendar('renderEvents', $.parseJSON(jsonResponse) )
                alert("予定を更新しました。");
            },
            error: function() {
            }
        });
    }
    $('#calendar').fullCalendar('unselect');
}
    
/* 予定入力フォームの削除ボタンクリックイベント. */
function deleteSchedule() {
    // ユーザCD
    var userCd = $("#userCd").val();
    // スケジュールID
    var id = $("#scheduleId").val();
    
    var startYmd = moment(formatNengappi($('#inputYmdFrom').val() + "00時00分00", 1));
    var endYmd = moment(formatNengappi($('#inputYmdTo').val() + "23時59分59", 1));
    var allDayCheck = $('#allDayCheck').prop("checked");
    if (!allDayCheck) {
        startYmd = moment(formatNengappi($('#inputYmdHmFrom').val(), 1));
        endYmd = moment(formatNengappi($('#inputYmdHmTo').val(), 1));
    }
    if (endYmd.diff(startYmd, 'days') > 0) {
        endYmd = endYmd.add(+1, "days");
    }
    
    var eventData;
    if ($('#inputTitle').val()) {
        eventData = {
            user_cd: $("#userCd").val(),
            id: $("#scheduleId").val(),
        };
        $.ajax({
            url: "http://localhost:8080/delete",
            type: "POST",
            data: JSON.stringify(eventData),
            success: function(jsonResponse) {
                // 再描画
                $('#calendar').fullCalendar('removeEvents');
                $('#calendar').fullCalendar('renderEvents', $.parseJSON(jsonResponse) )
                alert("予定を削除しました。");
            },
            error: function() {
            }
        });
    }
    $('#calendar').fullCalendar('unselect');
}
    
/* 終日チェックボックスクリックイベント. */
function allDayCheckClick(element) {
    if (element && element.checked) {
        var startYmd = moment(formatNengappi($("#inputYmdFrom").val(), 0));
        var endYmd = moment(formatNengappi($("#inputYmdTo").val(), 0));
        var startYmdHm = moment(startYmd.format("YYYY-MM-DD") + " " + "00:00");
        var endYmdHm = moment(startYmd.format("YYYY-MM-DD") + " " + "23:59");
        $("#inputYmdHmFrom").val(startYmdHm.format("YYYY年MM月DD日 HH時mm分"));
        $("#inputYmdHmTo").val(endYmdHm.format("YYYY年MM月DD日 HH時mm分"));
        $('.ymdHm').show();
        $('.ymd').hide();
    }
    else {
        var startYmd = moment(formatNengappi($("#inputYmdFrom").val(), 0));
        var endYmd = moment(formatNengappi($("#inputYmdTo").val(), 0));
        var startYmdHm = moment(startYmd.format("YYYY-MM-DD") + " " + moment().format("HH") + ":00:00");
        var endYmdHm = moment(startYmd.format("YYYY-MM-DD") + " " + moment().format("HH") + ":00:00").add(1, "hours");
        $("#inputYmdHmFrom").val(startYmdHm.format("YYYY年MM月DD日 HH時mm分"));
        $("#inputYmdHmTo").val(endYmdHm.format("YYYY年MM月DD日 HH時mm分"));
    
        $('.ymd').hide();
        $('.ymdHm').show();
    }
}
    
/* 年月日の形式を変換する. */
function formatNengappi(nengappi, flg) {
    var ret = nengappi.replace("年", "-").replace("月", "-").replace("日", "");
    if (flg == 1){
        ret = nengappi.replace("年", "-").replace("月", "-").replace("日", " ").replace("時",":").replace("分",":").replace(" ","");
    }
    return ret;
}