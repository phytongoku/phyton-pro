import discord
import random

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')




#Tu código aquí
@bot.command
async def historia(ctx):
    await ctx.send("hola amigo")
async def hola(ctx):
    await ctx.send("he escuchado que quieres escuchar una historia")
async def si(ctx):
    await ctx.send("La contaminación ha acompañado al ser humano desde la Revolución Industrial, cuando el aumento de fábricas y el uso de combustibles fósiles comenzaron a degradar el aire, el agua y el suelo. Con el tiempo, el crecimiento poblacional, la industrialización masiva y el consumismo han agravado el problema, generando residuos plásticos, emisiones tóxicas y destrucción de ecosistemas.
sus impactos son devastadores: cambio climático, pérdida de biodiversidad, enfermedades respiratorias y contaminación de océanos. Sin embargo, aún estamos a tiempo de cambiar. Reduciendo nuestro consumo, usando energías limpias y exigiendo políticas ambientales, podemos construir un futuro más sostenible.
¡El planeta necesita acción hoy! 🌎💚")
    await ctx.send("entonces te gusto")
    await ctx.send("bien,aqui hay unas recomendaciones")
async def basura(ctx, tipo_residuo: str):
    tipo= tipo_residuo.lower()
    recomendaciones = {
        "organico": "🟤 *Bolsas marrones* (residuos orgánicos: comida, cáscaras, restos vegetales).",
        "plastico": "🟡 *Bolsas amarillas* (envases plásticos, botellas, bolsas).",
        "papel": "🔵 *Bolsas azules* (papel, cartón limpio, periódicos).",
        "vidrio": "🟢 *Bolsas verdes* (botellas de vidrio, frascos).",
        "metal": "🔘 *Bolsas grises* (latas, aluminio, metales).",
        "peligroso": "🔴 *Bolsas rojas* (baterías, medicamentos, químicos).",
        "textil": "⚪ *Bolsas blancas* (ropa vieja, trapos)."}
    
    if tipo in recomendaciones:
        await ctx.send(f"Para *{tipo}*, usa: {recomendaciones[tipo]}")
    else:
        opciones = "\n".join([f"- {key}" for key in recomendaciones.keys()])
        await ctx.send(
            f"*Tipo de residuo no reconocido.*\n"
            f"Opciones válidas:\n{opciones}\n\n"
            "Ejemplo: $basura plastico"
        )
@bot.command()
async def mas contaminadores(ctx):
    await ctx.send{"la basura que mas contamina son los humos contaminantes,desechos plasticos,el uracio,el carbon,baterias,celulares viejos"}
client.run("Token")