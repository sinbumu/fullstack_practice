import * as React from 'react';
import { Slide } from '../components/slide';

export default function Home() {
  const thirdSlideTitle = '울퉁불퉁하다';
  
  return (
    <div>
      <h1>gatsby TEST web</h1>
      <Slide title="매끈매끈하다" >매끈매끈한~</Slide>
      <Slide title="푱푱하다">
        푱푱한
      </Slide>
      <Slide title={thirdSlideTitle}>울퉁불퉁한
      </Slide>
    </div>
  );
}
