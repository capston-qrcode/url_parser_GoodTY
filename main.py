import pandas as pd
from urllib.parse import urlparse

def add_http_to_urls(file_path, output_file_path):

    df = pd.read_csv(file_path)    # CSV 파일 읽기

    def ensure_http(url):# http:// 또는 https://가 없는 URL에 http:// 추가
        if not url.startswith('http://') and not url.startswith('https://'):
            return 'http://' + url
        return url

    df['url'] = df['url'].apply(ensure_http) #URL 컬럼에서 http:// 또는 https://가 없는 부분 수정

    df.to_csv(output_file_path, index=False) #수정된 데이터를 새로운 CSV 파일로 저장

    print(f"수정된 URL을 저장한 CSV 파일이 {output_file_path}에 저장되었습니다.")

add_http_to_urls('phishing_data.csv', 'output_file_path.csv')
df = pd.read_csv('output_file_path.csv')

def parse_url_text(url):
    # URL을 파싱
    parsed_url = urlparse(url)

    # 파싱된 URL 정보 저장
    netloc = parsed_url.netloc  # 도메인 (예: www.example.com)
    scheme = parsed_url.scheme
    path = parsed_url.path      # 경로 (예: /some/path/)
    query = parsed_url.query    # 쿼리 문자열 (예: ?id=123)
    fragment = parsed_url.fragment  # 프래그먼트(앵커) (예: #section1)

    # 결과를 딕셔너리 형태로 반환
    return {
        'url': url,
        'scheme': scheme,
        'domain': netloc,
        'path': path,
        'query': query,
        'fragment': fragment
    }

# 각 URL 텍스트를 파싱하여 결과 저장
parsed_urls = df['url'].apply(parse_url_text)

# 파싱된 데이터를 데이터프레임으로 변환
parsed_df = pd.DataFrame(parsed_urls.tolist())

# 파싱된 결과를 CSV 파일로 저장
parsed_df.to_csv('parsed_url_text.csv', index=False)

print("URL 파싱이 완료되었습니다. 결과는 'parsed_url_text.csv'에 저장되었습니다.")