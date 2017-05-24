from scipy import integrate

'''assumptions made:
    we are integrating over such miniscule time periods every time (like one millisecond), that it does not matter if we do a left, right, or midpoint reimann sum
    We are already so close to being basically the actual integral that the error won't be of any issue
    when integrating from velocity to displacement, even though we use the newly calculated velocity, it should, in theory, be not that much different from the last one, so it won't makde
    any noticable error. If it does, we can always average to make it better
    '''

class integrator(object):
    def __init__(self, dh):
        self.dh = dh

    def integrate(self):
        time, acc = self.dh.getPlottableVersion('acceleration')

        veloc = integrate.cumtrapz(acc, time, initial=0)
        self.dh.addDataStream('velocity')
        self.dh.setDataStream('velocity', time, veloc)


        disp = integrate.cumtrapz(veloc, time, initial=0)
        self.dh.addDataStream('displacement')
        self.dh.setDataStream('displacement', time,  disp)
        return self.dh

    def __adjust(self): #adjust values
        '''
        shift acceleration graph, since we start with max accceleration, and it has 0 when at eq pos
        velocity should be fine
        need to create position stream, which is an adjusted version of displacement: integration assumes we start at 0, but really we start at max
        TODO: check acceleration is negative when going down, or just make sure everything is in right direction
        '''


