if (cx.data < 300)&(cy.data < 220):
            pos_x += 0.01
            pos_y += 0.01
            set_pos(pos_x,pos_y,pos_z)
        elif (cx.data < 300)&(cy.data >= 220)&(cy.data <= 260):
            pos_y += 0.01
            set_pos(pos_x,pos_y,pos_z)
        elif (cx.data < 300)&(cy.data > 260):
            pos_x -= 0.01
            pos_y += 0.01
            set_pos(pos_x,pos_y,pos_z)
        elif (cx.data >= 300)&(cx.data <= 340)&(cy.data < 220):
            pos_x -= 0.01
            set_pos(pos_x,pos_y,pos_z)
        elif (cx.data > 340)&(cy.data < 220):
            pos_x += 0.01
            pos_y -= 0.01
            set_pos(pos_x,pos_y,pos_z)
        elif (cx.data > 340)&(cy.data >= 220)&(cy.data <= 260):
            pos_y -= 0.01
            set_pos(pos_x,pos_y,pos_z)
        elif (cx.data > 340)&(cy.data > 260):
            pos_x -= 0.01
            pos_y -= 0.01
            set_pos(pos_x,pos_y,pos_z)
        elif (cx.data >= 300)&(cx.data <= 340)&(cy.data > 260):
            pos_x += 0.01
            set_pos(pos_x,pos_y,pos_z)
        else:
            pos_x += 0.0445
            pos_y += 0.05
            pos_z -= 0.10
            set_pos(pos_x,pos_y,pos_z)
            break
