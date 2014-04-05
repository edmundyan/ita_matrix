# ITA
import form
import itasearch
import itaserver

import time

def main():
  ita = itaserver.ITAServer()

  options = {
    'type': 'roundtrip',
    'from1': 'San Francisco International, CA (SFO)',
    'to1': 'New York, NY - All airports',
    'out_date': '6/15/2014',
    'out_span': form.Form.SPAN_DAY_AFTER,
    'return_date': '6/22/2014',
    'return_span': form.Form.SPAN_TWO_DAY
  }
  search = itasearch.ITASearch(ita, options)
  search.execute()

  results = search.results()

  print results



if __name__ == '__main__':
  main()