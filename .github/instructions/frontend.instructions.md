# 프론트엔드 개발 지침

## HTML 코딩 컨벤션

1. 시맨틱 태그 사용

   - `header`, `nav`, `main`, `article`, `section`, `footer` 등의 시맨틱 태그를 적절히 활용
   - `div`와 `span`은 꼭 필요한 경우에만 사용

2. 들여쓰기

   - 2칸 공백 사용
   - 중첩된 요소는 반드시 들여쓰기 적용

3. 속성 작성 순서
   ```html
   id -> class -> name -> data-* -> src, for, type, href -> title, alt ->
   aria-*, role
   ```

## CSS 스타일 가이드

1. 클래스 네이밍

   - BEM(Block Element Modifier) 방법론 준수
   - 케밥 케이스(kebab-case) 사용

   ```css
   .block__element--modifier .memo-card__title--highlighted;
   ```

2. 선택자 규칙

   - ID 선택자 사용 최소화
   - 태그 선택자와 결합한 과도한 체이닝 금지
   - 클래스 기반 스타일링 지향

3. 미디어 쿼리
   - 모바일 퍼스트 접근
   - 주요 브레이크포인트:
     ```css
     /* 모바일 */
     @media (min-width: 320px) {
       ...;
     }
     /* 태블릿 */
     @media (min-width: 768px) {
       ...;
     }
     /* 데스크탑 */
     @media (min-width: 1024px) {
       ...;
     }
     ```

## Bootstrap 활용 가이드

1. 그리드 시스템

   - 12컬럼 그리드 시스템 활용
   - 반응형 클래스 적극 활용 (`col-sm`, `col-md`, `col-lg`)

2. 컴포넌트 커스터마이징

   - Bootstrap 변수 재정의는 `_variables.scss`에서 관리
   - 커스텀 스타일은 별도의 파일로 분리

3. 유틸리티 클래스
   - 간단한 스타일링은 유틸리티 클래스 활용
   - 복잡한 스타일링은 커스텀 클래스 작성

## JavaScript 코딩 스타일

1. 변수 선언

   - `const`와 `let` 사용 (`var` 사용 금지)
   - 의미있는 변수명 사용
   - 카멜케이스(camelCase) 준수

2. 함수 작성

   - 화살표 함수 활용
   - 함수는 한 가지 역할만 수행
   - 비동기 처리는 async/await 사용

3. 이벤트 핸들링
   - 이벤트 위임 패턴 활용
   - 디바운싱/쓰로틀링 적용
   ```javascript
   const debounce = (fn, delay) => {
     let timeout;
     return (...args) => {
       clearTimeout(timeout);
       timeout = setTimeout(() => fn(...args), delay);
     };
   };
   ```

## 웹 접근성 가이드라인

1. ARIA 레이블

   - 모든 상호작용 요소에 적절한 ARIA 레이블 추가
   - 의미가 명확하지 않은 이미지에 대체 텍스트 제공

2. 키보드 접근성

   - 모든 상호작용 요소는 키보드로 접근 가능하도록 구현
   - 포커스 순서 논리적으로 구성
   - 포커스 표시자 명확하게 표시

3. 색상 대비
   - WCAG 2.1 기준 준수
   - 텍스트와 배경색 간 최소 대비율 4.5:1 유지

## 성능 최적화

1. 이미지 최적화

   - WebP 포맷 사용
   - 적절한 이미지 크기 사용
   - 지연 로딩 적용

2. 자바스크립트 최적화

   - 번들 크기 최소화
   - 코드 스플리팅 적용
   - 중요하지 않은 스크립트는 defer 또는 async 적용

3. CSS 최적화
   - 사용하지 않는 CSS 제거
   - Critical CSS 인라인 적용
   - CSS 번들링 및 최소화

## 테스트

1. 크로스 브라우저 테스트

   - 주요 브라우저에서 동작 확인
   - 모바일 환경 테스트

2. 반응형 테스트
   - 다양한 화면 크기에서 레이아웃 확인
   - 터치 이벤트 동작 확인

## 문서화

1. 컴포넌트 문서화

   - 컴포넌트의 용도와 사용법 명시
   - 필수 속성과 선택 속성 구분하여 설명

2. 주석 작성
   - 복잡한 로직에 대한 설명 추가
   - TODO 주석은 이슈 트래커와 연동
