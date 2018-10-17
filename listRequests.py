import json
from random import *
from token import *
from time import gmtime, strftime

token = getToken()
transactionId = 'OA0841:SOA0815V1.0:'+strftime("%Y%m%d%H%M%S", gmtime())+str(randint(0000000000000000000000000,9999999999999999999999999))

def payloadConsultarPortifolio(msisdn):
	 payload = 	{  
                   "MessageHeader":{  
                      "TransactionId":transactionId,
                      "BusinessKey":"0000",
                      "Timestamp":"2012-12-13T12:12:12"
                   },
                   "Credentials":{  
                      "AppId":"OA0841",
                      "Token":token
                   },
                   "CatalogoProduto":{  
                      "IdCanal":"600",
                      "TipoCliente":"00",
                      "TipoRecarga":"01"
                   }
                }
	 return payload

def payloadComprarPacote(msisdn):
	payload = {
                  "Servico": {"NumeroServico": msisdn},
                  "ProdutoBundle": {"idBundle": "D10"},
                  "Canal": {"IdCanal": "APP"},
                  "ParametroOperacao": {"Operation": "1"
                   },
                   "MessageHeader": 
                   {
                      "Timestamp":  "2017-05-30T11:34:11"             ,
                      "Credentials": {
                         "AppId": "OA0841"
                      },
                      "TransactionId": "OA0841:SOA0131V1.0:AAAAMMDDHHMMSSZZZ:000:000000000000000000000066"
                   },
                   "token": token
                }
	return payload

def payloadConsultarInfoAssinante(msisdn):
	payload = 	{
				   "MessageHeader":{
				   "TransactionId":transactionId,
    			   "Timestamp":"2012-12-13T12:12:12",
      			   "Credentials":{
         		   "AppId":"OA0841"
				      }
				   },
				   "token": token,
				   "MSISDN": msisdn
				}

	return payload


def payloadConcedeDireitos(msisdn):
	payload = 	{
				    "MessageHeader": {
      				"TransactionId": transactionId,
      				"AppId": "OA0841",
      				"Timestamp": "29052017093859"
				    },
				    "token": token,
				    "EventoRecarga": {
                    "idEventoRecarga": "00",
                    "dataRecarga": "20080929010000",
                    "idCliente": msisdn,
                    "tipoProdutoRecarga": "00",
                    "idBolso": "54",
                    "idProdutoRecarga": "137263",
                    "subCanal": "601",
                    "valorFace": "100000",
                    "validade": "31"
				    }
			  	}
	return payload

def payLoadConsultarContaDetalhadaPre(msisdn):
	payload = 	{
                   "token": token,
                    "ContaDetalhadaPreRequest": {
                      "Ator": {
                        "sistema": "APP"
                      },
                      "numTT": "1234",
                      "dataInicio": "01/05/2017",
                      "dataFim": "12/01/2017",
                      "msisdn": msisdn,
                      "tpRequisicao": "-2",
                      "tpChamada": "-2",
                      "listaSecoes": "-2"
    }
			  	}
	return payload


def payLoadConsultarHistoricoAssinante(msisdn):
	payload = 	{
                    "token": token,
                    "ContaDetalhadaPreRequest": {
                      "Ator": {
                        "sistema": "APP"
                      },
                      "numTT": "1234",
                      "dataInicio": "01/04/2017",
                      "dataFim": "26/05/2017",
                      "msisdn": msisdn,
                      "tpRequisicao": "-2",
                      "tpChamada": "-2",
                      "listaSecoes": "-2"
                    }
			  	}
	return payload

def payLoadTrocaCreditoConsultar(msisdn):
	payload = {
				"Token": token,
				"NumeroAssinante": msisdn,
				"Cliente": "APP",
				"Operacao": "1"
			  }
	return payload

def payLoadTrocaCreditoExecutar(msisdn):
	payload = {
				"Token": token,
				"NumeroAssinante": msisdn,
				"Cliente": "APP",
			    "Operacao": "2",
			    "BolsoOrigem": "51",
			    "TaxaConversao": "60:10240",
			    "Amount": "1",
			    "BolsoDestino": "54"
			  }
	return payload

def getNames(msisdn):
	 return {
			 'ConsultarPortifolio' : payloadConsultarPortifolio(msisdn),
			 'ComprarPacote' : payloadComprarPacote(msisdn),
			 'ConsultarInfoAssinante' : payloadConsultarInfoAssinante(msisdn),
			 'ConcedeDireitos' : payloadConcedeDireitos(msisdn),
			 'ConsultarContaDetalhadaPre' : payLoadConsultarContaDetalhadaPre(msisdn),
			 'ConsultarHistoricoAssinante' : payLoadConsultarHistoricoAssinante(msisdn),
			 'TrocaCredito' : payLoadTrocaCreditoConsultar(msisdn),
			 'TrocaCredito ' : payLoadTrocaCreditoExecutar(msisdn)
			}