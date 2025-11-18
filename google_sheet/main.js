const SheetApiClientFactory = require('./sheet_api_client_factory');
const SheetDownloader = require('./sheet_downloader');

async function main() {
  try {
    const sheetApiClient = await SheetApiClientFactory.create();
    const downloader = new SheetDownloader(sheetApiClient);

    // 아래와 같은 구글 스프레드시트 주소 중 d와 edit 사이에 들어있는 부분이 스프레드시트의 ID 값 입니다.
    
    // MVP 모델 설문조사 정리한 시트 식별자.
    const spreadsheetId = '1N2-fqkGzDHhe-dBr6RUPoQYibhl4z7RQHwgTonOJRqk';

    const notice = await downloader.downloadToJson(
      spreadsheetId,
      'Form Responses 1',
      'downloaded/notice.json',
    );

    console.log(notice); 
    
  } catch (e) {
    console.error(e);
  }
}

main();


