import cherrypy
from library import dna_rna_cleaner
from library import lenght_seq
from library import dna_to_rna
from library import percentage_gc
from library import reverse
from library import complementary

class MultiRouteApp:
    @cherrypy.expose
    def index(self):
        return """
        <html>
          <head><title>Multiple Routes Demo</title></head>
          <body>
            <h2>Paste your sequence in the box then click! </h2>

            <form method="post" action="/clean">
              <input type="text" name="input_string" />
              <button type="submit">Clean</button>
            </form>
            <br>

            <form method="post" action="/lenght">
              <input type="text" name="input_string" />
              <button type="submit">Lenght</button>
            </form>
            <br>

            <form method="post" action="/dna_to_rna">
              <input type="text" name="input_string" />
              <button type="submit">DNA to RNA</button>
            </form>
            <br>

            <form method="post" action="/percentage_gc">
              <input type="text" name="input_string" />
              <button type="submit">GC %</button>
            </form>
            <br>

             <form method="post" action="/reverse">
              <input type="text" name="input_string" />
              <button type="submit">Reverse</button>
            </form>
            <br>

            <form method="post" action="/complementary">
              <input type="text" name="input_string" />
              <button type="submit">Complementary</button>
            </form>
            <br>

            <form method="post" action="/rev_and_compl">
              <input type="text" name="input_string" />
              <button type="submit">Reverse and Complementary</button>
            </form>
            <br>

          </body>
        </html>
        """

    # --------- Individual action routes ---------
    @cherrypy.expose
    def clean(self, input_string=None):
        sequence = dna_rna_cleaner(input_string)
        return self._result_page("Cleaned sequence: ", sequence)

    @cherrypy.expose
    def lenght(self, input_string=None):
        cleaned_seq = dna_rna_cleaner(input_string)
        sequence = lenght_seq(cleaned_seq)
        return self._result_page("Sequence lenght: ", sequence)

    @cherrypy.expose
    def dna_to_rna(self, input_string=None):
        cleaned_seq = dna_rna_cleaner(input_string)
        sequence = dna_to_rna(cleaned_seq)
        return self._result_page("RNA sequence: ", sequence)
    
    @cherrypy.expose
    def percentage_gc(self, input_string=None):
        cleaned_seq = dna_rna_cleaner(input_string)
        sequence = percentage_gc(cleaned_seq)
        return self._result_page("GC %: ", sequence)
    
    @cherrypy.expose
    def reverse(self, input_string=None):
        cleaned_seq = dna_rna_cleaner(input_string)
        sequence = reverse(cleaned_seq)
        return self._result_page("Reverse sequence: ", sequence)
    
    @cherrypy.expose
    def complementary(self, input_string=None):
        cleaned_seq = dna_rna_cleaner(input_string)
        sequence = complementary(cleaned_seq)
        return self._result_page("Complementary sequence: ", sequence)
    
    @cherrypy.expose
    def rev_and_compl(self, input_string=None):
        cleaned_seq = dna_rna_cleaner(input_string)
        rev_sequence = reverse(cleaned_seq)
        complementary_seq = complementary(rev_sequence)
        return self._result_page("Complementary sequence: ", complementary_seq)

    # --------- Helper to render result pages ---------
    def _result_page(self, title, result):
        return f"""
        <html>
          <head><title>{title} Result</title></head>
          <body>
            <h3>{title} {result}</h3>
            <a href="/">Back to home</a>
          </body>
        </html>
        """

if __name__ == "__main__":
    cherrypy.quickstart(MultiRouteApp())
