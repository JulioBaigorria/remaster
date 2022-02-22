# from django.core.management.base import BaseCommand, CommandError


# class Command(BaseCommand):
#     help = 'The help information for this command'
#
#     def add_arguments(self, parser):
#         parser.add_argument('first', type=int, help='A number less than 100')
#         # parser.add_argument('-arg')
#         parser.add_argument('second', nargs=3, type=str, help='Three strings')
#         parser.add_argument('--option1', default='if not is None for default', help='The optional value')
#         parser.add_argument('--option2', action='store_true', help='True if passed')
#
#     def handle(self, *args, **options):
#         # print('Command: mycommand')
#         # print('Second Line!')
#         # print(f'Options {options["first"]}')
#         # print(f'Options {options["option1"]}')
#         if options["first"] < 100:
#             self.stdout.write(self.style.SUCCESS('Good job the number is less than 100'))
#         else:
#             raise CommandError('That number is greater than 100')
#         for value in options['second']:
#             self.stdout.write(f'{value}')
#         self.stdout.write(f'the value of --option1 is {options["option1"]}')
#
#         if options['option2']:
#             self.stdout.write(self.style.SUCCESS('Option2 is True'))
#         else:
#             self.stdout.write(self.style.WARNING('Option2 is False'))
