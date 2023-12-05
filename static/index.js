document.getElementById("button").addEventListener("click", function () {
  // Ajax 요청 생성
  var xhr = new XMLHttpRequest();
  xhr.open('GET', '/main', true);

  // 요청 완료 시의 콜백 함수
  xhr.onload = function () {
    if (xhr.status === 200) {
      console.log('API 호출 성공');
      // 서버 응답에 따른 추가 동작 가능
      window.location.href = '/main'; // 서버에서 수행한 동작에 따라 페이지 이동
    } else {
      console.error('API 호출 실패. 상태 코드: ' + xhr.status);
    }
  };

  // 요청 전송
  xhr.send();
});