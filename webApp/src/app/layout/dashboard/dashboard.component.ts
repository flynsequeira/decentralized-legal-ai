import { Component, OnInit } from '@angular/core';
import { MatTableDataSource } from '@angular/material';
import { RestService } from '../../shared/services/rest.service';

export interface Currency {
    value: string;
    viewValue: string;
  }


@Component({
    selector: 'app-dashboard',
    templateUrl: './dashboard.component.html',
    styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {
    cryptoSelected = '';
    currencySel = '';
    cyptos: Currency[] = [
        {value: 'ETH', viewValue: 'Ethereum'},
        {value: 'DASH', viewValue: 'Dash'},
        {value: 'BCH', viewValue: 'Bitcoin Cash'},
        {value: 'LTC', viewValue: 'Litecoin'}
      ];

    currencies: Currency[] = [
        {value: 'AUD', viewValue: 'Australia Dollar'},
        {value: 'GBP', viewValue: 'Great Britain Pound	'},
        {value: 'EUR', viewValue: 'Euro'},
        {value: 'JPY', viewValue: 'Japan Yen'},
        {value: 'USD', viewValue: 'USA Dollar'}
      ];

    constructor(private _rest: RestService) {
    }

    ngOnInit() {}

    submitForm() {

        console.log(this.cryptoSelected);
        console.log(this.currencySel);
        console.log('clicked');
    }

}
