//제출버튼
const btnAjax = document.querySelector(".submit");

//익명이 누군지를 세기 위한 count변수
let count = 0;

//만약 버튼을 클릭했을때
btnAjax.addEventListener("click", (e) => {
    //contents에는 댓글 내용을 담는다.
    const contents = document.querySelector('.reply-text').value;

    const param = {
        'contents' : contents,
        'user_id' : {{request.user.id}}, //사용자가 접속한 아아디
        'post_id' : {{date.id}}, 
    };

    //버튼을 클릭하고 ajax를 통해서 서버와 통신을 시작한다.
    $.ajax({
        url: {% url 'reply' %}, //댓글을 쓰기위한 URL
        type: "POST", //POST방식으로 보낸다.
        headers: {
            "X-CSRFTOKEN": '{{csrf_token}}' //POST방식으로  보낼때 CSRF TORKEN을 같이 보내기 위해서
        },
        data : JSON.stringify(param), //JS개체를 JSON 문자열로 변환한다.

    //댓글 작성 성공 했을때
    success: (data) => {
        alert("댓글 작성 성공");
        console.log(data);
        count ++; //카운터 하나씩 증가
        //서버에서 전송받은 response data를 이용하여 새로고침을 안해도 동적으로 HTML에 추가한다.
        $(".submit").after("<div class='comment'><span style='font-weight: bold'> 익명" + count + ":&nbsp;</span> <span>" + data.contents + "</span></div>");

        },
    //댓글 작성 실패시
    error : () => {
        alert("댓글 작성이 실패했습니다.");
        },
    });
});

