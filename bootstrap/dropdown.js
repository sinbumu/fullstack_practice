import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Container, Dropdown } from 'react-bootstrap';

export default function DropdownPage() {
  return (
    <Container className="pt-3">
      <Dropdown>
        <Dropdown.Toggle>학과선택</Dropdown.Toggle>
        <Dropdown.Menu>
          <Dropdown.Item href="">소프트웨어</Dropdown.Item>
          <Dropdown.Item href="">인공지능</Dropdown.Item>
          <Dropdown.Item href="https://swgs.kookmin.ac.kr/swgs/major/ai-application.do">인공지능응용</Dropdown.Item>
          <Dropdown.Item href="">자동차공학</Dropdown.Item>
        </Dropdown.Menu>
      </Dropdown>
    </Container>
  );
}


