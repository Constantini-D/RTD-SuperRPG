CODIGO
+++++++


Codigo Mago
===============

pythons
---------

Aqui está a função que representa o mago:

.. code-block:: python

    class Mago(Npc, Cajado):

        def __init__(self, nome, life, armor, mana, inte):
            self.classe = __class__.__name__
            super().__init__(nome, life, armor, mana, inte, None)
            Cajado.__init__(self)

        @gritar
        def magia(self, magia):
            return f'{magia}'

Neste código, pode-se ver que a Classe Mago recebe a herança da  classe NPC


Objetos
-------------
.. csv-table:: Objetos do Mago
    :header: nome, inteligência, mana
    :widths: 15, 10, 10

    Mithrandir, 60, 100
    veigar, 100,100