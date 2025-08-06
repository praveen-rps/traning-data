import { TestBed } from '@angular/core/testing';

import { DemoService } from './demo.service';

describe('DemoService', () => {
  let service: DemoService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(DemoService);
  });

  it('should be postive when both are positive', () => {
    const result = service.multiply(2,3);
    expect(result).toEqual(6);
  });
  it('should be zero when one is zero', () => {
    const result = service.multiply(2,0);
    expect(result).toEqual(0);
  });
  it('should be postive when both are negative', () => {
    const result = service.multiply(-2,-3);
    expect(result).toEqual(6);
  });
  it('should be negative when one is negative', () => {
    const result = service.multiply(-2,3);
    expect(result).toEqual(-6);
  });
});
