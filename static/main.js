document.addEventListener('Loaded', function () {
    
    document.getElementById('open').addEventListener('click', function () {
        callServerAPI('/api/water/openA');
    });

    document.getElementById('close').addEventListener('click', function () {
        callServerAPI('/api/water/closeA');
    });

    document.getElementById('open1').addEventListener('click', function () {
        callServerAPI('/api/water/openB');
    });

    document.getElementById('close1').addEventListener('click', function () {
        callServerAPI('/api/water/closeB');
    });
});

function callServerAPI(apiEndpoint) {
    // Ajax 요청 생성
    var xhr = new XMLHttpRequest();
    xhr.open('GET', apiEndpoint, true);

    // 요청 완료 시의 콜백 함수
    xhr.onload = function () {a
        if (xhr.status === 200) {
            console.log('API 호출 성공');
            // 서버 응답에 따른 추가 동작 가능
        } else {
            console.error('API 호출 실패. 상태 코드: ' + xhr.status);
        }
    };

    // 요청 전송
    xhr.send();
}
