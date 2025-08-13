import { TestBed } from '@angular/core/testing';

import { UserService } from './user.service';

describe('UserService', () => {
  let service: UserService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(UserService);
  });

  it('should return postive result if both are positive', ()=>{
    const result = service.multiply(1,2);
    expect(result).toBe(2);
  });

  it('should return zero result if one of them is zero', ()=>{
    const result = service.multiply(0,2);
    expect(result).toBe(0);
  });

  it('should return postive result if both are negative', ()=>{
    const result = service.multiply(-1,-2);
    expect(result).toBe(2);
  });
  it('should return negative result if one of them is negative', ()=>{
    const result = service.multiply(-1,2);
    expect(result).toBe(-2);
  });
});
