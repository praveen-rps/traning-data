import { TestBed } from '@angular/core/testing';
import {HttpClientTestingModule, HttpTestingController} 
from '@angular/common/http/testing';
import { DemoService } from './demo.service';


describe('DemoService', () => {
  let service: DemoService;
  let httpMock : HttpTestingController;
  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(DemoService);
    httpMock = TestBed.inject(HttpTestingController)
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

  it('should return Bret when given userid 1',()=>{
    const id=1
    const mockResponse = {id:1,name:"Leanne Graham",username:"Bret",
      email:"Sincere@april.biz",phone:"1-770-736-8031 x56442"
    }
    service.getUserById(1).subscribe(id => {
      expect(id).toEqual(mockResponse);
    });
  const req = httpMock.expectOne('https://jsonplaceholder.typicode.com/users/'+id);
  expect(req.request.method).toEqual('GET');
  })


});
